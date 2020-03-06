const ch = require('cheerio');
var fs = require('fs');

let buildDir = './dist/simulation-widget/';
let outputFile = '../pynbsim/index.html';
let requiredReads = 0;
let completedReads = 0;
let $;
let scriptSources = [];
let scriptReads = [];
let contentString = '';

if (!String.prototype.splice) {
    /**
     * {JSDoc}
     *
     * The splice() method changes the content of a string by removing a range of
     * characters and/or adding new characters.
     *
     * @this {String}
     * @param {number} start Index at which to start changing the string.
     * @param {number} delCount An integer indicating the number of old chars to remove.
     * @param {string} newSubStr The String that is spliced in.
     * @return {string} A new string with the spliced substring.
     */
    String.prototype.splice = function(start, delCount, newSubStr) {
        return this.slice(0, start) + newSubStr + this.slice(start + Math.abs(delCount));
    };
}

fs.readFile(buildDir + 'index.html', 'utf8', function(err, contents) {
    if(!err) {
        contentString = contents;
        $ = ch.load(contents);
        $("script").each(function(i, s){
            requiredReads++;
            scriptSources[i] = s.attribs.src;
            fs.readFile(buildDir + s.attribs.src, function(err, scriptContents) {
                scriptReads[i] = scriptContents;
                completedReads++;
                compileAfterReads();
            });
        });
    } else {
        throw err;
    }
});

function compileAfterReads() {
    if (completedReads == requiredReads) {
        for(let i in scriptSources) {
            let startSearch = contentString.indexOf(scriptSources[i]);
            let insertLocation = contentString.indexOf('>', startSearch) + 1;
            contentString = contentString.splice(insertLocation, 0, scriptReads[i]);
            contentString = contentString.replace(' src="' + scriptSources[i] + '"', '');
        }
        $ = ch.load(contentString);
        $("script").each(function(i, s){
            delete s.attribs.src;
        });
        fs.readFile(buildDir + 'styles.css', function(err, style) {
            contentString = contentString.replace('<link rel="stylesheet" href="styles.css">', '<style>' + style + '</style>');
            fs.writeFile(outputFile, contentString, function() {});
        })
    }
}

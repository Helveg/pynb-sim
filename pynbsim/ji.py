"""
    Jupyter Interface:: This class contains the core methods to interface with the
    Jupyter notebook.
"""
import os, sys
from IPython.core.display import display, HTML
from .progress import add_progress_listener
from .format import format

def widget():
    display(HTML(format("""
    <script>
        cellDiv = $("div.cell.code_cell:contains('import pynbsim')");
        cellDiv.addClass('widget_cell');
        inputDiv = cellDiv.find('div.input');
        console.log("Initializing pynbsim widget in div:", cellDiv);
        labelShown = 'Hide widget init'; labelHidden = 'Show widget init';
        if(!cellDiv.attr('loaded')) {
            inputDiv.hide();
            inputHidden = true;
            function toggleInput() {
            if(inputHidden) {
                inputDiv.show();
                $("#toggleInput").find('span').html(labelShown);
            } else {
                inputDiv.hide();
                $("#toggleInput").find('span').html(labelHidden);
            }
            inputHidden = !inputHidden;
            }
            $("<div id='toggleInput'></div>")
                .css('position', 'relative')
                .css('top', '-4px')
                .css('left', '-4px')
                .css('cursor', 'pointer')
                .click(toggleInput)
                .insertBefore(cellDiv)
                .append(
                    $("<span>" + labelHidden + "</span>").css('color', '#999').css('font-style', 'italic')
                ).append({powered_by})

            cellDiv.attr('loaded', true);
        }
    </script>
    """)))
    with open(os.path.join(os.path.dirname(__file__), "index.html")) as f:
        display(HTML(f.read()))

def progress_text(token):
    display(HTML(format("""
        <div id="{{|token|}}">Simulation starting...</div>
        <script>
            {{|tag|}}
            $(".inj-{{|token|}}").remove();
            console.log("Adding progress text label?")
            console.log($('#{{|token|}}').length);
            progressTextLabel = $('#{{|token|}}');
            console.log("Progress cell?", progressTextCodeCell);
            console.log("Progress label?", progressTextLabel);
            progressTextCodeCell.prepend({{|powered_by_header|}}.addClass('inj-{{|token|}}'));
        </script>
        <style>
            /* Keep the injected blocks alive as long as this output exists */
            .pynbsim-injected-block.inj-{{|token|}} {
                display: block !important;
            }
        </style>""",
        token=token,
        token_var=token.replace("-", "_"),
        tag=tag_code_cell(token, "progressTextCodeCell")
    )))

def tag_code_cell(unique, var="codeCell"):
    return format("""
            {{|var|}} = $("div.cell.code_cell:contains('{{|unique|}}')");
            console.log("var", {{|var|}});
        """,
        unique=unique,
        var=var
    )

def init_page():
    display(HTML("""<script>
        $.getScript("https://kit.fontawesome.com/aceb3af2d4.js", function(){

        });
        $(`<style>
            .powered-by-header {
                width: 100%;
                margin-bottom: 4px;
            }

            .powered-by {
                float: right;
                border: #F79862 1.2px solid;
                border-radius: 10px;
                padding: 4px;
                color: wheat;
                font-style: italic;
                background-color: #F79862;
            }

            .powered-by a {
                color: white;
                font-style: normal;
            }
        </style>`).appendTo( "head" );"""))

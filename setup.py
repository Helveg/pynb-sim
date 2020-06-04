import setuptools

with open(os.path.join(os.path.dirname(__file__), pynbsim, "__init__.py"), "r") as f:
    for line in f:
        if "__version__ = " in line:
            exec(line)
            break

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='pynb-sim',
     version=__version__,
     author="Robin De Schepper",
     author_email="robingilbert.deschepper@unipv.it",
     description="Widgets & tools for large scale simulations inside of Python jupyter notebooks",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/Helveg/pynb-sim",
     license='GPLv3',
     packages=setuptools.find_packages(),
     include_package_data=True,
     package_data={"pynbsim": ["*.html"]},
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
     install_requires=[

     ],
     extras_require={
      "dev": ["sphinx", "sphinx_rtd_theme"]
     }
 )

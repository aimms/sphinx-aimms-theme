from distutils.core import setup
import setuptools
import sys


setup(
    
    name = "sphinx_aimms_theme",
    version = '1.0.0',
    license = "MIT",
    packages= ['sphinx_aimms_theme'],
    url = "https://github.com/pietroalbini/sphinx-themes",
    author = "AIMMS User Support",
    author_email = "support@aimms.com",

    description = "AIMMS theme for Sphinx",

    
    entry_points = {
        'sphinx.html_themes': [
            'sphinx_aimms_theme = sphinx_aimms_theme',
        ]        
    },
    install_requires=[
       'sphinx',
       'sphinx_rtd_theme',
    ],

)
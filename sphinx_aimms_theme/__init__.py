from os import path
from sphinx.util import logging
import AIMMSDomain

def setup(app):

    # Import the necessary python files for the custom AIMMS lexer, and the custom AIMMS domain
    from .AIMMSLexer import AIMMSLexer
    from .AIMMSDomain import AIMMSDomain
    from pygments.formatters import HtmlFormatter
    app.add_lexer("aimms", AIMMSLexer())
    logger = logging.getLogger(__name__)
    logger.info('AIMMS Lexer added')
    app.add_domain(AIMMSDomain)
    logger.info('AIMMS Domain added')
    
    # See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
    app.add_html_theme('sphinx_aimms_theme', path.abspath(path.dirname(__file__)))
    
    # including javascript for the copy code functionality
    app.add_js_file('copycode.js')
    app.add_js_file('https://cdn.jsdelivr.net/npm/clipboard@1/dist/clipboard.min.js')
    
    # including css for the AIMMS declaration icons attached to the AIMMS Domain
    app.add_css_file('declaration_icons.css')
    




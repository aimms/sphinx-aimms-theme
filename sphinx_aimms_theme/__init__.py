from os import path
from sphinx.util import logging
import AIMMSDomain

def setup(app):
    from .AIMMSLexer import AIMMSLexer
    #import AIMMSDomain
    #from .AIMMSDomain import AIMMSDomain
    from pygments.formatters import HtmlFormatter
    app.add_lexer("aimms", AIMMSLexer())
    logger = logging.getLogger(__name__)
    logger.info('\nAIMMS Lexer added')
    #app.add_domain(AIMMSDomain)
    
    app.add_html_theme('sphinx_aimms_theme', path.abspath(path.dirname(__file__)))



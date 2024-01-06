"""A Pygments lexer for the command examples"""
import re

from pygments.lexer import RegexLexer, bygroups
from pygments.token import *

__all__ = ("CommandLexer",)

class CommandLexer(RegexLexer):
    """Simple lexer to highlight arguments of commands."""
    
    name = 'Command'
    aliases = ['command']
    filenames = ['*.command']
    
    tokens = {
        'root': [
            (r'^(\/)([^\S]+)', bygroups(Name.Tag, Text)),
            (r'[&][0-9abcdefklmnoruABCDEFKLMNORU]', Keyword),
            (r'[\[\{<]', Punctuation, 'option'),
            (r'\w', Text)
        ],
        'option': [
            (r'\|', Punctuation),
            (r'[^\[\{<>\}\|\]]+', Name.Tag),
            (r'[\[\{<]', Punctuation, '#push'),
            (r'[\]\}>]', Punctuation, '#pop')
        ]
    }
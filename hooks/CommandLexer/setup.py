#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name = 'commandlexer',
    version = '1.0.0',
    packages = find_packages(),
    entry_points = 
    """
    [pygments.lexers]
    commandlexer = commandlexer.command_lexer:CommandLexer
    """
)
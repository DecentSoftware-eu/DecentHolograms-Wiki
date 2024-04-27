#
# A simple hook that replaces any appearances of \| with just |.
#
# There is an inconsistency between GitHub flavourited Markdown and Python Markdown.
# GFM treats | inside a table cell as a table cell separator, even if it was put in
# inline code while Python Markdown does not.
#
# The only way to prevent this is to escape it by prefixing it with a back slash (\).
# Unfortunately does this cause issues on Python-Markdown, as it renders inline code
# content as-is without special treatments whatsoever, meaning that `\|` will be
# rendered as <code>\|</code> in the end.
#
# This hook now turns any \| into | when the site is being processed, so that it
# shows as <code>|<code> in the final page while not breaking tables on GitHub.
#
import re

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import File, Files
from mkdocs.structure.pages import Page

def on_page_content(
        html: str, page: Page, config: MkDocsConfig, files: Files 
):
    return re.sub(r"\\\|","|",html)
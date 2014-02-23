"""HTML: MIN writer NW test

Testing suite to write HTML in the MIN style.

"""

import lexor
from lexor.command.test import compare_with

DOCUMENT = """<!--Copyright: ML-->
<html>
<!--This comment is not copied in the min style-->
<br/>
<!--ML: My comment-->
content.
<!--JS: My name is John Smith-->
</html>
"""
EXPECTED = """<!--Copyright: ML--><html><br/> content. </html>"""


def test_min():
    """html.writer.min.nw """
    doc, _ = lexor.parse(DOCUMENT, 'html')
    doc.style = 'min'
    doc.defaults = {
        'comment': 'Copyright:'
    }
    compare_with(str(doc), EXPECTED)

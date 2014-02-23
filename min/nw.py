"""HTML: MIN NodeWriter

Collection of NodeWriter objects to write an html is a compressed form.

"""

import re
from lexor.core.writer import NodeWriter
import lexor.core.elements as core
RE = re.compile(r'\s+')


class DefaultNW(NodeWriter):
    """Default way of writing HTML elements in the min style. """

    def start(self, node):
        if isinstance(node, core.ProcessingInstruction):
            self.write('<%s ' % node.name)
            return
        att = ' '.join(['%s="%s"' % (k, v) for k, v in node.items()])
        self.write('<%s' % node.name)
        if att != '':
            self.write(' %s' % att)
        if isinstance(node, core.Void):
            self.write('/>')
        else:
            self.write('>')

    def end(self, node):
        if node.child is None:
            if isinstance(node, core.ProcessingInstruction):
                self.write('?>')
            elif isinstance(node, core.RawText):
                self.write('</%s>' % node.name)
        else:
            self.write('</%s>' % node.name)


class CommentNW(NodeWriter):
    """Writes `<!-- ... -->`. """
    match = None

    def start(self, node):
        match_str = self.writer.defaults['comment']
        if match_str != '':
            self.match = re.match(match_str, node.data)
        else:
            self.match = None
        if self.match:
            self.write('<!--')

    def data(self, node):
        if self.match:
            self.write(node.data)

    def end(self, node):
        if self.match:
            self.write('-->')


class DoctypeNW(NodeWriter):
    """Writes `<!DOCTYPE ...>`. """

    def start(self, node):
        self.write('<!DOCTYPE ')

    def data(self, node):
        self.write(re.sub(RE, ' ', node.data).strip())

    def end(self, node):
        self.write('>')


class CDataNW(NodeWriter):
    """Writes `<![CDATA[ ... ]]>`. """

    def start(self, node):
        self.write('<![CDATA[')

    def data(self, node):
        data = node.data.split(']]>')
        for index in xrange(len(data)-1):
            self.write(data[index] + ']]]]><![CDATA[>')
        self.write(data[-1])

    def end(self, node):
        self.write(']]>')


def printable_prev(node):
    """Check if any of node.prev is a printable text or entity
    node."""
    while node.prev is not None and node.prev.name in ['#entity', '#text']:
        if node.prev.data.strip() == '':
            node = node.prev
        else:
            return True
    return False


def printable_next(node):
    """Check if any of node.next is a printable text or entity node.
    """
    while node.next is not None and node.next.name in ['#entity', '#text']:
        if node.next.data.strip() == '':
            node = node.next
        else:
            return True
    return False


class TextNW(NodeWriter):
    """Writes all text nodes with no spaces. """

    def data(self, node):
        text = re.sub(RE, ' ', node.data)
        if text.strip() == '' and text == ' ':
            if not printable_prev(node) and not printable_next(node):
                return
        self.write(text)

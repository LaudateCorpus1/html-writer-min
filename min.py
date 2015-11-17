"""HTML: MIN Writer Style

The minimum style removes all the extra blank spaces and comments to
have a compressed document.

There are a few comments that we may want to keep. To make a few
exceptions we can modify the default `comment`.

For instance if example.html is:

    <!--Copyright: ML-->
    <html>
    <!--This comment is not copied in the min style-->
    <br/>
    <!--ML: My comment-->
    content.
    <!--JS: My name is John Smith-->
    </html>

Then the output of

    lexor example.html to html~min@comment="Copyright:"~

will be

    <!--Copyright: ML--><html><br/> content. </html>

"""

from lexor import init, load_aux

INFO = init(
    version=(0, 0, 1, 'final', 0),
    lang='html',
    type='writer',
    description='Writes HTML files to minimize the file size.',
    git={
        'host': 'github',
        'user': 'jmlopez-rod',
        'repo': 'html-writer-min'
    },
    author={
        'name': 'Manuel Lopez',
        'email': 'jmlopez.rod@gmail.com'
    },
    docs='http://jmlopez-rod.github.io/lexor-lang/html-writer-min',
    license='BSD License',
    path=__file__
)
MOD = load_aux(INFO)['nw']
DEFAULTS = {
    'comment': '',
}
MAPPING = {
    '#text': MOD.TextNW,
    '#comment': MOD.CommentNW,
    '#doctype': MOD.DoctypeNW,
    '#cdata-section': MOD.CDataNW,
    '__default__': MOD.DefaultNW,
}

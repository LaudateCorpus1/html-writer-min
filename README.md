Lexor Language: HTML min style writer
=====================================

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

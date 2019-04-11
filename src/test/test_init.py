from markyp_html import DOCTYPE,\
                        html,\
                        head,\
                        body,\
                        base,\
                        title,\
                        link,\
                        meta,\
                        script,\
                        style,\
                        join,\
                        webpage

def test_DOCTYPE():
    assert DOCTYPE().markup == "<!DOCTYPE html>"
    assert str(DOCTYPE()) == "<!DOCTYPE html>"

def test_html():
    assert html().markup == "<html ></html>"
    assert str(html(something="something")) == '<html something="something"></html>'
    assert str(html(head(), body())) == "<html >\n<head ></head>\n<body ></body>\n</html>"

def test_head():
    assert head().markup == "<head ></head>"
    assert head(title("Page Title")).markup == "<head >\n<title >Page Title</title>\n</head>"

def test_body():
    assert body().markup == "<body ></body>"
    assert body(script("one"), script("two"), attr="attr").markup ==\
        '<body attr="attr">\n<script >\none\n</script>\n<script >\ntwo\n</script>\n</body>'

def test_base():
    assert base().markup == "<base >"
    assert base(target="_blank", base="example.com").markup == '<base target="_blank" base="example.com">'

def test_title():
    assert title("Page Title").markup == "<title >Page Title</title>"

def test_link():
    assert link(rel="stylesheet", type="text/css", href="theme.css").markup ==\
        '<link rel="stylesheet" type="text/css" href="theme.css">'
    assert link.css(href="theme.css").markup ==\
        '<link rel="stylesheet" type="text/css" href="theme.css">'

def test_meta():
    assert meta(name="viewport", content="width=device-width, initial-scale=1.0").markup ==\
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">'

    assert meta.author("Joe").markup ==\
        '<meta name="author" content="Joe">'
    assert meta.charset("UTF-8").markup ==\
        '<meta charset="UTF-8">'
    assert meta.charset().markup ==\
        '<meta charset="UTF-8">'
    assert meta.description("Short description of the page").markup ==\
        '<meta name="description" content="Short description of the page">'
    assert meta.keywords("one, two, three").markup ==\
        '<meta name="keywords" content="one, two, three">'
    assert meta.viewport().markup ==\
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
    assert meta.viewport("width=device-width, initial-scale=1.0").markup ==\
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">'

def test_script():
    assert script('document.getElementById("demo").innerHTML = "Hello JavaScript!";').markup ==\
        '<script >\ndocument.getElementById("demo").innerHTML = "Hello JavaScript!";\n</script>'

    assert script.ref("script.js").markup == '<script src="script.js"></script>'

def test_style():
    assert style("h1 {color:red;}\np {color:blue;}").markup == '<style >\nh1 {color:red;}\np {color:blue;}\n</style>'

def test_join():
    assert join() == ""
    assert join(None, None, None, None, None) == ""
    assert join("foo") == "foo"
    assert join("foo", "bar", "baz") == "foo bar baz"
    assert join(None, "foo", None, "bar", None, "baz", None) == "foo bar baz"

    # Duplicates are not filtered.
    assert join("foo", "foo") == "foo foo"

def test_webpage():
    assert webpage(
            "markyp-html webpage() test",
            "Should be successful.",
            page_title="Page Title",
            base_element=base(target="_blank", base="example.com"),
            metadata=(
                meta(name="viewport", content="width=device-width, initial-scale=1.0"),
                meta(charset="UTF-8")
            ),
            head_elements=(
                link(rel="stylesheet", type="text/css", href="theme.css"),
            ),
            javascript=(
                script('document.getElementById("demo").innerHTML = "Hello JavaScript!";'),
            ),
            class_="my-fancy-html-body",
            attr="body-attribute"
        ).markup == "\n".join((
            '<!DOCTYPE html>',
            '<html >',
            '<head >',
            '<title >Page Title</title>',
            '<base target="_blank" base="example.com">',
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
            '<meta charset="UTF-8">',
            '<link rel="stylesheet" type="text/css" href="theme.css">',
            '</head>',
            '<body attr="body-attribute" class="my-fancy-html-body">',
            'markyp-html webpage() test',
            'Should be successful.',
            '<script >\ndocument.getElementById("demo").innerHTML = "Hello JavaScript!";\n</script>',
            '</body>',
            '</html>'
        ))

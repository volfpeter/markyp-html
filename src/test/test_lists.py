from markyp_html.lists import li,\
                              ol,\
                              ul,\
                              dl,\
                              dt,\
                              dd

def test_li():
    assert li("List item").markup == "<li >List item</li>"

def test_ol():
    assert ol(li("Item 1"), li("Item 2")).markup ==\
        "<ol >\n<li >Item 1</li>\n<li >Item 2</li>\n</ol>"

def test_ul():
    assert ul(li("Item 1"), li("Item 2")).markup ==\
        "<ul >\n<li >Item 1</li>\n<li >Item 2</li>\n</ul>"

def test_dl():
    assert dl("dt and dt elements should be here").markup ==\
        "<dl >\ndt and dt elements should be here\n</dl>"

def test_dt():
    assert dt("Term in a description list.").markup ==\
        "<dt >Term in a description list.</dt>"

def test_dd():
    assert dd("Term in a description list.").markup ==\
        "<dd >Term in a description list.</dd>"

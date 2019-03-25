from markyp_html.text import h1,\
                             h2,\
                             h3,\
                             h4,\
                             h5,\
                             h6,\
                             p

def test_h1():
    assert h1("Text element content").markup == "<h1 >Text element content</h1>"

def test_h2():
    assert h2("Text element content").markup == "<h2 >Text element content</h2>"

def test_h3():
    assert h3("Text element content").markup == "<h3 >Text element content</h3>"

def test_h4():
    assert h4("Text element content").markup == "<h4 >Text element content</h4>"

def test_h5():
    assert h5("Text element content").markup == "<h5 >Text element content</h5>"

def test_h6():
    assert h6("Text element content").markup == "<h6 >Text element content</h6>"

def test_p():
    assert p("Text element content").markup == "<p >Text element content</p>"

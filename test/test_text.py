from markyp_html.text import *

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

def test_StyledTextFactory():
    factory = StyledTextFactory("fancy-text")
    assert factory.base_css_class == "fancy-text"
    assert factory.h1("Text element content").markup == '<h1 class="fancy-text">Text element content</h1>'
    assert factory.h2("Text element content").markup == '<h2 class="fancy-text">Text element content</h2>'
    assert factory.h3("Text element content").markup == '<h3 class="fancy-text">Text element content</h3>'
    assert factory.h4("Text element content").markup == '<h4 class="fancy-text">Text element content</h4>'
    assert factory.h5("Text element content").markup == '<h5 class="fancy-text">Text element content</h5>'
    assert factory.h6("Text element content").markup == '<h6 class="fancy-text">Text element content</h6>'
    assert factory.p("Text element content").markup == '<p class="fancy-text">Text element content</p>'

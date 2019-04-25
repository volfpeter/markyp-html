from markyp_html.inline import *

def test_InlineElement():
    assert InlineElement("Text should be in-line with the tags.").markup ==\
        "<InlineElement >Text should be in-line with the tags.</InlineElement>"

def test_a():
    assert a("Visit W3Schools.com!", href="https://www.w3schools.com").markup ==\
        '<a href="https://www.w3schools.com">Visit W3Schools.com!</a>'

def test_abbr():
    assert abbr("WHO", title="World Health Organization").markup ==\
        '<abbr title="World Health Organization">WHO</abbr>'

def test_b():
    assert b("Bold text").markup == "<b >Bold text</b>"

def test_bdi():
    assert bdi("Bi-Directional Isolation").markup ==\
        "<bdi >Bi-Directional Isolation</bdi>"

def test_bdo():
    assert bdo("Bi-Directional Override", dir="rtl").markup ==\
        '<bdo dir="rtl">Bi-Directional Override</bdo>'

def test_br():
    assert br().markup == "<br >"

def test_cite():
    assert cite("Citation").markup == "<cite >Citation</cite>"

def test_code():
    assert code("markyp-html <code> element.").markup ==\
        "<code >markyp-html &lt;code&gt; element.</code>"

def test_data():
    assert data("Pi", value=3.1415).markup == '<data value="3.1415">Pi</data>'

def test_del_():
    assert del_("deleted part").markup == "<del >deleted part</del>"

def test_dfn():
    assert dfn("Defining Instance of a Term").markup ==\
        "<dfn >Defining Instance of a Term</dfn>"

def test_em():
    assert em("emphasized text").markup == "<em >emphasized text</em>"

def test_i():
    assert i("italic text").markup == "<i >italic text</i>"

def test_img():
    assert img(src="smiley.gif", alt="Smiley face", height=42, width=42).markup ==\
        '<img src="smiley.gif" alt="Smiley face" height="42" width="42">'
    assert img(src="smiley.gif", height=42, width=42).markup ==\
        '<img src="smiley.gif" height="42" width="42">'
    assert img(src="smiley.gif", class_="my-img", height=42, width=42).markup ==\
        '<img src="smiley.gif" height="42" width="42" class="my-img">'

    assert img.placeholder(100, 200).markup ==\
        '<img src="https://via.placeholder.com/100x200?text=Placeholder" alt="Placeholder">'
    assert img.placeholder(1, 1).markup ==\
        '<img src="https://via.placeholder.com/10x10?text=Placeholder" alt="Placeholder">'
    assert img.placeholder(100, 200, class_="my-img").markup ==\
        '<img src="https://via.placeholder.com/100x200?text=Placeholder" alt="Placeholder" class="my-img">'
    assert img.placeholder(100, 200, text="/Escaped&text").markup ==\
        '<img src="https://via.placeholder.com/100x200?text=%2FEscaped%26text" alt="/Escaped&text">'

def test_ins():
    assert ins("newly inserted text").markup == "<ins >newly inserted text</ins>"

def test_mark():
    assert mark("marked text").markup == "<mark >marked text</mark>"

def test_q():
    assert q("quoted text").markup == "<q >quoted text</q>"

def test_s():
    assert s("incorrect text").markup == "<s >incorrect text</s>"

def test_samp():
    assert samp("sample output").markup == "<samp >sample output</samp>"

def test_small():
    assert small("small text").markup == "<small >small text</small>"

def test_span():
    assert span("inline group of text", class_="color:blue;").markup ==\
        '<span class="color:blue;">inline group of text</span>'

def test_strong():
    assert strong("strong text").markup == "<strong >strong text</strong>"

def test_sub():
    assert sub("subscript text").markup == "<sub >subscript text</sub>"

def test_sup():
    assert sup("superscript text").markup == "<sup >superscript text</sup>"

def test_u():
    assert u("underlined, misspelled text").markup == "<u >underlined, misspelled text</u>"

def test_var():
    assert var("Variable").markup == "<var >Variable</var>"

def test_wbr():
    assert wbr("word break opportunity").markup == "<wbr >word break opportunity</wbr>"

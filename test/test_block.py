from markyp_html.block import *

def test_address():
    assert address("Contact info", hr(), "Circle Street 31415").markup ==\
        "<address >\nContact info\n<hr >\nCircle Street 31415\n</address>"

def test_article():
    assert article("Part 1", hr(), "Part 2").markup ==\
        "<article >\nPart 1\n<hr >\nPart 2\n</article>"

def test_aside():
    assert aside("Part 1", hr(), "Part 2").markup ==\
        "<aside >\nPart 1\n<hr >\nPart 2\n</aside>"

def test_blockquote():
    assert blockquote("There are two hard things in CS: cache invalidation, naming things and indexing.").markup ==\
        "<blockquote >\nThere are two hard things in CS: cache invalidation, naming things and indexing.\n</blockquote>"

def test_div():
    assert div("Part 1", hr(), "Part 2", class_="fancy-div").markup ==\
        '<div class="fancy-div">\nPart 1\n<hr >\nPart 2\n</div>'

def test_embed():
    assert embed(src="https://www.w3schools.com").markup ==\
        '<embed src="https://www.w3schools.com">'

def test_figure():
    assert figure("Content: for example an image", figcaption("Figure caption")).markup ==\
        "<figure >\nContent: for example an image\n<figcaption >Figure caption</figcaption>\n</figure>"

def test_figcaption():
    assert figcaption("Figure caption").markup == "<figcaption >Figure caption</figcaption>"

def test_footer():
    assert footer("Part 1", hr(), "Part 2").markup ==\
        "<footer >\nPart 1\n<hr >\nPart 2\n</footer>"

def test_header():
    assert header("Part 1", hr(), "Part 2").markup ==\
        "<header >\nPart 1\n<hr >\nPart 2\n</header>"

def test_hr():
    assert hr().markup == "<hr >"

def test_iframe():
    assert iframe(src="https://www.w3schools.com").markup ==\
        '<iframe src="https://www.w3schools.com"></iframe>'

def test_main():
    assert main("Part 1", hr(), "Part 2").markup ==\
        "<main >\nPart 1\n<hr >\nPart 2\n</main>"

def test_nav():
    assert nav("First link", "Second link", 'Third link').markup ==\
        "<nav >\nFirst link\nSecond link\nThird link\n</nav>"

def test_noscript():
    assert noscript("Your browser does not support JavaScript!").markup ==\
        "<noscript >\nYour browser does not support JavaScript!\n</noscript>"

def test_pre():
    assert pre("Preformatted\ntext").markup ==\
        "<pre >\nPreformatted\ntext\n</pre>"

def test_section():
    assert section("Part 1", hr(), "Part 2").markup ==\
        "<section >\nPart 1\n<hr >\nPart 2\n</section>"

def test_template():
    assert template("<markup >Content</markup>", hr(), "Normal text").markup ==\
        "<template >\n<markup >Content</markup>\n<hr >\nNormal text\n</template>"

from markyp_html.entities import Entity,\
                                 amp,\
                                 apos,\
                                 cent,\
                                 copy,\
                                 euro,\
                                 gt,\
                                 lt,\
                                 nbsp,\
                                 pound,\
                                 quot,\
                                 reg,\
                                 times,\
                                 yen

def test_entity():
    assert Entity("").markup == ""
    assert Entity("foo").markup == "foo"
    assert Entity("<>").markup == "<>"
    assert Entity("&foo;").markup == "&foo;"

def test_amp():
    assert amp.markup == "&amp;"

def test_apos():
    assert apos.markup == "&apos;"

def test_cent():
    assert cent.markup == "&cent;"

def test_copy():
    assert copy.markup == "&copy;"

def test_euro():
    assert euro.markup == "&euro;"

def test_gt():
    assert gt.markup == "&gt;"

def test_lt():
    assert lt.markup == "&lt;"

def test_nbsp():
    assert nbsp.markup == "&nbsp;"

def test_pound():
    assert pound.markup == "&pound;"

def test_quot():
    assert quot.markup == "&quot;"

def test_reg():
    assert reg.markup == "&reg;"

def test_times():
    assert times.markup == "&times;"

def test_yen():
    assert yen.markup == "&yen;"

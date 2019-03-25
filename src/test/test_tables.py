from markyp_html.tables import caption,\
                               table,\
                               thead,\
                               tbody,\
                               tfoot,\
                               tr,\
                               th,\
                               td

def test_caption():
    assert caption("Table caption").markup ==\
        "<caption >Table caption</caption>"

def test_table():
    assert table(caption("Table caption")).markup ==\
        "<table >\n<caption >Table caption</caption>\n</table>"

def test_thead():
    assert thead(tr(th("Column 1"), th("Column 2"))).markup ==\
        "<thead >\n<tr >\n<th >Column 1</th>\n<th >Column 2</th>\n</tr>\n</thead>"

def test_tbody():
    assert tbody(tr(td("Data 1"), td("Data 2"))).markup ==\
        "<tbody >\n<tr >\n<td >Data 1</td>\n<td >Data 2</td>\n</tr>\n</tbody>"

def test_tfoot():
    assert tfoot(tr(th("Column footer 1"), th("Column footer 2"))).markup ==\
        "<tfoot >\n<tr >\n<th >Column footer 1</th>\n<th >Column footer 2</th>\n</tr>\n</tfoot>"

def test_tr():
    assert tr(th("Column 1"), th("Column 2")).markup ==\
        "<tr >\n<th >Column 1</th>\n<th >Column 2</th>\n</tr>"

def test_th():
    assert th("Column").markup ==\
        "<th >Column</th>"

def test_td():
    assert td("Table data").markup ==\
        "<td >Table data</td>"

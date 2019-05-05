from markyp_html.forms import *

def test_form():
    assert str(form("First", "Second", action="/action_page.php", method="get")) ==\
        '<form action="/action_page.php" method="get">\nFirst\nSecond\n</form>'

def test_button():
    assert str(button("Click here", **{"type": "button"})) ==\
        '<button type="button">Click here</button>'

def test_option():
    assert str(option("Test", value="test")) ==\
        '<option value="test">Test</option>'

def test_optgroup():
    assert str(optgroup(label="Option group")) ==\
        '<optgroup label="Option group"></optgroup>'

def test_datalist():
    assert str(datalist()) ==\
        '<datalist ></datalist>'

def test_fieldset():
    assert str(fieldset("Group of related form elements")) ==\
        '<fieldset >\nGroup of related form elements\n</fieldset>'

def test_input_():
    assert str(input_(type_="text", name="input_1")) ==\
        '<input name="input_1" type="text">'
    assert str(input_(type_="submit", value="Submit")) ==\
        '<input value="Submit" type="submit">'

    assert input_.button(name="input-1").markup ==\
        '<input name="input-1" type="button">'

    assert input_.checkbox(name="input-1").markup ==\
        '<input name="input-1" type="checkbox">'

    assert input_.email(name="input-1").markup ==\
        '<input name="input-1" type="email">'

    assert input_.file(name="input-1").markup ==\
        '<input name="input-1" type="file">'

    assert input_.hidden(name="input-1").markup ==\
        '<input name="input-1" type="hidden">'

    assert input_.number(name="input-1").markup ==\
        '<input name="input-1" type="number">'

    assert input_.password(name="input-1").markup ==\
        '<input name="input-1" type="password">'

    assert input_.radio(name="input-1").markup ==\
        '<input name="input-1" type="radio">'

    assert input_.search(name="input-1").markup ==\
        '<input name="input-1" type="search">'

    assert input_.submit(name="input-1").markup ==\
        '<input name="input-1" type="submit">'

    assert input_.text(name="input-1").markup ==\
        '<input name="input-1" type="text">'

    assert input_.time(name="input-1").markup ==\
        '<input name="input-1" type="time">'

def test_label():
    assert str(label("Label", form_id="form_1", input_id="input_1")) ==\
        '<label form="form_1" for="input_1">Label</label>'

def test_legend():
    assert str(legend("Fieldset caption")) ==\
        '<legend >Fieldset caption</legend>'

def test_meter():
    assert str(meter("2 out of 10", value=2, min=0, max=10)) ==\
        '<meter value="2" min="0" max="10">2 out of 10</meter>'

def test_output():
    assert str(output(name="output_field", **{"for": "input_1 input_2"})) ==\
        '<output name="output_field" for="input_1 input_2"></output>'

def test_progress():
    assert str(progress(value="42", max="100")) ==\
        '<progress value="42" max="100"></progress>'

def test_select():
    assert str(select(option("First", value="first"), option("Second", value="second"))) ==\
        '<select >\n<option value="first">First</option>\n<option value="second">Second</option>\n</select>'

def test_textarea():
    assert str(textarea("Text", rows=4, cols=80)) ==\
        '<textarea rows="4" cols="80">\nText\n</textarea>'

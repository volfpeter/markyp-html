"""
HTML table elements.

See http://www.wikiwand.com/en/HTML_element#/Tables.
"""

from markyp.elements import Element


__all__ = ("caption", "table", "thead", "tbody", "tfoot", "tr", "th", "td")


class caption(Element):
    """
    `<caption></caption>` element.

    See https://www.w3schools.com/tags/tag_caption.asp.
    """

    __slots__ = ()

    @property
    def inline_children(self) -> bool:
        return True


class table(Element):
    """
    `<table></table>` element.

    See https://www.w3schools.com/tags/tag_table.asp.
    """
    __slots__ = ()


class thead(Element):
    """
    `<thead></thead>` element.

    See https://www.w3schools.com/tags/tag_thead.asp.
    """
    __slots__ = ()


class tbody(Element):
    """
    `<tbody></tbody>` element.

    See https://www.w3schools.com/tags/tag_tbody.asp.
    """
    __slots__ = ()


class tfoot(Element):
    """
    `<tfoot></tfoot>` element.

    See https://www.w3schools.com/tags/tag_tfoot.asp.
    """
    __slots__ = ()


class tr(Element):
    """
    `<tr></tr>` element.

    See https://www.w3schools.com/tags/tag_tr.asp.
    """
    __slots__ = ()


class th(Element):
    """
    `<th></th>` element.

    See https://www.w3schools.com/tags/tag_th.asp.
    """

    __slots__ = ()

    @property
    def inline_children(self) -> bool:
        return True


class td(Element):
    """
    `<td></td>` element.

    See https://www.w3schools.com/tags/tag_td.asp.
    """

    __slots__ = ()

    @property
    def inline_children(self) -> bool:
        return True

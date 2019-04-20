"""
List and list item elements.
"""

from markyp.elements import Element


__all__ = ("li", "ol", "ul", "dl", "dt", "dd")


class li(Element):
    """
    `<li></li>` element.

    See https://www.w3schools.com/tags/tag_li.asp.
    """

    __slots__ = ()

    @property
    def inline_children(self) -> bool:
        return True


class ol(Element):
    """
    `<ol></ol>` element.

    See https://www.w3schools.com/tags/tag_ol.asp.
    """
    __slots__ = ()


class ul(Element):
    """
    `<ul></ul>` element.

    See https://www.w3schools.com/tags/tag_ul.asp.
    """
    __slots__ = ()


class dl(Element):
    """
    `<dl></dl>` element.

    See https://www.w3schools.com/tags/tag_dl.asp.
    """
    __slots__ = ()


class dt(Element):
    """
    `<dt></dt>` element.

    See https://www.w3schools.com/tags/tag_dt.asp.
    """

    __slots__ = ()

    @property
    def inline_children(self) -> bool:
        return True


class dd(Element):
    """
    `<dd></dd>` element.

    See https://www.w3schools.com/tags/tag_dd.asp.
    """

    __slots__ = ()

    @property
    def inline_children(self) -> bool:
        return True

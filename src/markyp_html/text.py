"""
HTML text elements (headings and paragraphs).
"""

from markyp.elements import Element


class TextElement(Element):
    """
    Base class for text elements.
    """

    __slots__ = ()

    @property
    def inline_children(self) -> bool:
        return True


class h1(TextElement):
    """
    `<h1></h1>` element.

    See https://www.w3schools.com/tags/tag_hn.asp.
    """
    __slots__ = ()


class h2(TextElement):
    """
    `<h2></h2>` element.

    See https://www.w3schools.com/tags/tag_hn.asp.
    """
    __slots__ = ()


class h3(TextElement):
    """
    `<h3></h3>` element.

    See https://www.w3schools.com/tags/tag_hn.asp.
    """
    __slots__ = ()


class h4(TextElement):
    """
    `<h4></h4>` element.

    See https://www.w3schools.com/tags/tag_hn.asp.
    """
    __slots__ = ()


class h5(TextElement):
    """
    `<h5></h5>` element.

    See https://www.w3schools.com/tags/tag_hn.asp.
    """
    __slots__ = ()


class h6(TextElement):
    """
    `<h6></h6>` element.

    See https://www.w3schools.com/tags/tag_hn.asp.
    """
    __slots__ = ()


class p(TextElement):
    """
    `<p></p>` element.

    See https://www.w3schools.com/tags/tag_p.asp.
    """
    __slots__ = ()

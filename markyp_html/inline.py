"""
In-line formatted HTML elements.

See http://www.wikiwand.com/en/HTML_element#/Inline_elements.
"""

from typing import Optional

from markyp import PropertyValue
from markyp.elements import Element, StandaloneElement


__all__ = (
    "InlineElement", "a", "abbr", "b", "bdi", "bdo", "br", "cite", "code",
    "data", "del_", "dfn", "em", "i", "img", "ins", "mark", "q", "s",
    "samp", "small", "span", "strong", "sub", "sup", "u", "var", "wbr"
)


class InlineElement(Element):
    """
    Element that formats its children in-line.
    """

    __slots__ = ()

    @property
    def inline_children(self) -> bool:
        return True


class a(InlineElement):
    """
    `<a></a>` element.

    See https://www.w3schools.com/tags/tag_a.asp.
    """
    __slots__ = ()


class abbr(InlineElement):
    """
    `<abbr></abbr>` element.

    See https://www.w3schools.com/tags/tag_abbr.asp.
    """
    __slots__ = ()


class b(InlineElement):
    """
    `<b></b>` element.

    See https://www.w3schools.com/tags/tag_b.asp.
    """
    __slots__ = ()


class bdi(InlineElement):
    """
    `<bdi></bdi>` element.

    See https://www.w3schools.com/tags/tag_bdi.asp.
    """
    __slots__ = ()


class bdo(InlineElement):
    """
    `<bdo></bdo>` element.

    See https://www.w3schools.com/tags/tag_bdo.asp.
    """
    __slots__ = ()


class br(StandaloneElement):
    """
    `<br>` element.

    See https://www.w3schools.com/tags/tag_br.asp.
    """
    __slots__ = ()


class cite(InlineElement):
    """
    `<cite></cite>` element.

    See https://www.w3schools.com/tags/tag_cite.asp.
    """
    __slots__ = ()


class code(InlineElement):
    """
    `<code></code>` element.

    See https://www.w3schools.com/tags/tag_code.asp.
    """
    __slots__ = ()


class data(InlineElement):
    """
    `<data></data>` element.

    See https://www.w3schools.com/tags/tag_data.asp.
    """
    __slots__ = ()


class del_(InlineElement):
    """
    `<del></del>` element.

    See https://www.w3schools.com/tags/tag_del.asp.
    """

    __slots__ = ()

    @property
    def element_name(self) -> str:
        return "del"


class dfn(InlineElement):
    """
    `<dfn></dfn>` element.

    See https://www.w3schools.com/tags/tag_dfn.asp.
    """
    __slots__ = ()


class em(InlineElement):
    """
    `<em></em>` element.

    See https://www.w3schools.com/tags/tag_em.asp.
    """
    __slots__ = ()


class i(InlineElement):
    """
    `<i></i>` element.

    See https://www.w3schools.com/tags/tag_i.asp.
    """
    __slots__ = ()


class img(StandaloneElement):
    """
    `<img>` element.

    See https://www.w3schools.com/tags/tag_img.asp.
    """

    __slots__ = ()

    def __init__(self, *, src: str, alt: Optional[str] = None, class_: Optional[str] = None, **kwargs: PropertyValue) -> None:
        super().__init__(
            **{"src": src, "alt": alt} if alt else {"src": src},
            class_=class_, **kwargs
        )

    @classmethod
    def placeholder(cls, w: int, h: int, *, text: str = "Placeholder", class_: Optional[str] = None, **kwargs: PropertyValue) -> "img":
        """
        Create a placeholder image element using the https://placeholder.com/ API.

        Keyword arguments that are not listed in the arguments section are turned
        into element attributes on the created image.

        The `src` keyword argument will be overwritten if specified by the caller.

        The `alt` argument will default to `text` if not specified by the caller.

        Arguments:
            w: The desired width of the element, minimum value is 10.
            h: The desired height of the element, minimum value is 10.
            text: Text to show on the placeholder image.
            class_: CSS classes to apply on the image.
        """
        from urllib.parse import urlencode
        w, h = max(w, 10), max(h, 10)
        kwargs["src"] = f"https://via.placeholder.com/{w}x{h}?{urlencode({'text': text})}"
        if "alt" not in kwargs:
            kwargs["alt"] = text
        return img(class_=class_, **kwargs)


class ins(InlineElement):
    """
    `<ins></ins>` element.

    See https://www.w3schools.com/tags/tag_ins.asp.
    """
    __slots__ = ()


class mark(InlineElement):
    """
    `<mark></mark>` element.

    See https://www.w3schools.com/tags/tag_mark.asp.
    """
    __slots__ = ()


class q(InlineElement):
    """
    `<q></q>` element.

    See https://www.w3schools.com/tags/tag_q.asp.
    """
    __slots__ = ()


class s(InlineElement):
    """
    `<s></s>` element.

    See https://www.w3schools.com/tags/tag_s.asp.
    """
    __slots__ = ()


class samp(InlineElement):
    """
    `<samp></samp>` element.

    See https://www.w3schools.com/tags/tag_samp.asp.
    """
    __slots__ = ()


class small(InlineElement):
    """
    `<small></small>` element.

    See https://www.w3schools.com/tags/tag_small.asp.
    """
    __slots__ = ()


class span(InlineElement):
    """
    `<span></span>` element.

    See https://www.w3schools.com/tags/tag_span.asp.
    """
    __slots__ = ()


class strong(InlineElement):
    """
    `<strong></strong>` element.

    See https://www.w3schools.com/tags/tag_strong.asp.
    """
    __slots__ = ()


class sub(InlineElement):
    """
    `<sub></sub>` element.

    See https://www.w3schools.com/tags/tag_sub.asp.
    """
    __slots__ = ()


class sup(InlineElement):
    """
    `<sup></sup>` element.

    See https://www.w3schools.com/tags/tag_sup.asp.
    """
    __slots__ = ()


class u(InlineElement):
    """
    `<u></u>` element.

    See https://www.w3schools.com/tags/tag_u.asp.
    """
    __slots__ = ()


class var(InlineElement):
    """
    `<var></var>` element.

    See https://www.w3schools.com/tags/tag_var.asp.
    """
    __slots__ = ()


class wbr(InlineElement):
    """
    `<wbr></wbr>` element.

    See https://www.w3schools.com/tags/tag_wbr.asp.
    """
    __slots__ = ()

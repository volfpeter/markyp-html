"""
HTML block elements.

See http://www.wikiwand.com/en/HTML_element#/Block_elements.
"""

from markyp.formatters import format_element_sequence, format_properties
from markyp.elements import Element, EmptyElement, StandaloneElement


__all__ = (
    "address", "article", "aside", "blockquote", "div", "embed",
    "figure", "figcaption", "footer", "header", "hr", "iframe",
    "main", "nav", "noscript", "pre", "section", "template"
)


class address(Element):
    """
    `<address></address>` element.

    See https://www.w3schools.com/tags/tag_address.asp.
    """
    __slots__ = ()


class article(Element):
    """
    `<article></article>` element.

    See https://www.w3schools.com/tags/tag_article.asp.
    """
    __slots__ = ()


class aside(Element):
    """
    `<aside></aside>` element.

    See https://www.w3schools.com/tags/tag_aside.asp.
    """
    __slots__ = ()


class blockquote(Element):
    """
    `<blockquote></blockquote>` element.

    See https://www.w3schools.com/tags/tag_blockquote.asp.
    """
    __slots__ = ()


class div(Element):
    """
    `<div></div>` element.

    See https://www.w3schools.com/tags/tag_div.asp.
    """
    __slots__ = ()


class embed(StandaloneElement):
    """
    `<embed>` element.

    See https://www.w3schools.com/tags/tag_embed.asp.
    """
    __slots__ = ()


class figure(Element):
    """
    `<figure></figure>` element.

    See https://www.w3schools.com/tags/tag_figure.asp.
    """
    __slots__ = ()


class figcaption(Element):
    """
    `<figcaption></figcaption>` element.

    See https://www.w3schools.com/tags/tag_figcaption.asp.
    """

    __slots__ = ()

    @property
    def inline_children(self) -> bool:
        return True


class footer(Element):
    """
    `<footer></footer>` element.

    See https://www.w3schools.com/tags/tag_footer.asp.
    """
    __slots__ = ()


class header(Element):
    """
    `<header></header>` element.

    See https://www.w3schools.com/tags/tag_header.asp.
    """
    __slots__ = ()


class hr(StandaloneElement):
    """
    `<hr>` element.

    See https://www.w3schools.com/tags/tag_hr.asp.
    """
    __slots__ = ()


class iframe(EmptyElement):
    """
    `<iframe></iframe>` element.

    See https://www.w3schools.com/tags/tag_iframe.asp.
    """
    __slots__ = ()


class main(Element):
    """
    `<main></main>` element.

    See https://www.w3schools.com/tags/tag_main.asp.
    """
    __slots__ = ()


class nav(Element):
    """
    `<nav></nav>` element.

    See https://www.w3schools.com/tags/tag_nav.asp.
    """
    __slots__ = ()


class noscript(Element):
    """
    `<noscript></noscript>` element.

    See https://www.w3schools.com/tags/tag_noscript.asp.
    """
    __slots__ = ()


class pre(Element):
    """
    `<pre></pre>` element.

    See https://www.w3schools.com/tags/tag_pre.asp.
    """
    __slots__ = ()


class section(Element):
    """
    `<section></section>` element.

    See https://www.w3schools.com/tags/tag_section.asp.
    """
    __slots__ = ()


class template(Element):
    """
    `<template></template>` element.

    See https://www.w3schools.com/tags/tag_template.asp.
    """

    __slots__ = ()

    def __str__(self) -> str:
        return f"<template {format_properties(self.properties)}>{format_element_sequence(self.children, element_formatter=str, inline=self.inline_children)}</template>"

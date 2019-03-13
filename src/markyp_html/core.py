"""
The base elements that are required in all HTML documents.
"""

from typing import Sequence, Union

from markyp import ElementType, IElement
from markyp.elements import Element, ElementSequence, StandaloneElement, StringElement
from markyp.formatters import format_properties


class DOCTYPE(IElement):
    """
    The HTML document type definition: `<!DOCTYPE html>`.
    """

    __slots__ = ()

    def __str__(self) -> str:
        return "<!DOCTYPE html>"


class html(Element):
    """
    `<html></html>` element.

    See https://www.w3schools.com/tags/tag_html.asp.
    """
    __slots__ = ()


class head(Element):
    """
    `<head></head>` element.

    See https://www.w3schools.com/tags/tag_head.asp.
    """
    __slots__ = ()


class body(Element):
    """
    `<body></body>` element.

    See https://www.w3schools.com/tags/tag_body.asp.
    """
    __slots__ = ()


class title(Element):
    """
    `<title></title>` element.

    See https://www.w3schools.com/tags/tag_title.asp.
    """
    __slots__ = ()


class link(StandaloneElement):
    """
    `<link>` element.

    See https://www.w3schools.com/tags/tag_link.asp.
    """
    __slots__ = ()


class meta(StandaloneElement):
    """
    `<meta>` element.

    See https://www.w3schools.com/tags/tag_meta.asp.
    """
    __slots__ = ()


class script(StringElement):
    """
    `<script></script>` element.

    See https://www.w3schools.com/tags/tag_script.asp.
    """

    __slots__ = ()

    def __str__(self) -> str:
        value = self.value or ""
        return f"<script {format_properties(self.properties)}>{value}</script>"


class style(StringElement):
    """
    `<style></style>` element.

    See https://www.w3schools.com/tags/tag_style.asp.
    """

    __slots__ = ()

    def __str__(self) -> str:
        value = self.value or ""
        return f"<style {format_properties(self.properties)}>{value}</style>"


def webpage(*body_elements: ElementType,
            page_title: str,
            metadata: Sequence[meta] = (),
            head_elements: Sequence[Union[link, script, style]] = (),
            javascript: Sequence[script] = ()) -> ElementSequence:
    """
    Higher order component that composes a valid HTML page from the received arguments.

    The positional arguments of the method must be the elements that build up the
    actual webpage, i.e. the content to place inside the `<body></body>` HTML tag.

    Arguments:
        page_title: The title of the webpage - mandatory keyword argument.
        metadata: The list of `meta` elements that describe the webpage.
        head_elements: Other elements that should be included in the head of the page
                       such as links, styles, and scripts.
        js_imports: `script` elements that import JavaScript packages such as JQuery
                    or execute some JavaScript code.
    """
    return ElementSequence(
        DOCTYPE(),
        html(
            head(
                title(page_title),
                *metadata,
                *head_elements,
            ),
            body(
                *body_elements,
                *javascript
            )
        )
    )

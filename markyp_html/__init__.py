"""
The base elements that are required in all HTML documents.
"""

from typing import Dict, Optional, Sequence, Union

from markyp import ElementType, IElement
from markyp.elements import Element, ElementSequence, StandaloneElement, StringElement
from markyp.formatters import format_properties


__author__ = "Peter Volf"
__copyright__ = "Copyright 2019, Peter Volf"
__email__ = "do.volfp@gmail.com"
__license__ = "MIT"
__url__ = "https://github.com/volfpeter/markyp-html"
__version__ = "0.1906.0"


__all__ = ("DOCTYPE", "html", "head", "body", "base", "title", "link", "meta", "script", "style")


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


class base(StandaloneElement):
    """
    `<base></base>` element.

    See https://www.w3schools.com/tags/tag_base.asp.
    """
    __slots__ = ()


class title(StringElement):
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

    @classmethod
    def css(cls, href: str) -> "link":
        """
        Creates a CSS `link` element that references the specified stylesheet.

        Arguments:
            href: The location of the referenced stylesheet.
        """
        return cls(rel="stylesheet", type="text/css", href=href)


class meta(StandaloneElement):
    """
    `<meta>` element.

    See https://www.w3schools.com/tags/tag_meta.asp.
    """
    __slots__ = ()

    @classmethod
    def author(cls, author_name: str) -> "meta":
        """
        Creates an author `meta` element.

        The `name` attribute of the created element will be `author` and
        its `content` attribute will be the `author_name`.

        Arguments:
            author_name: The name of the author of the page.
        """
        return cls(name="author", content=author_name)

    @classmethod
    def charset(cls, charset_name: str = "UTF-8") -> "meta":
        """
        Creates a charset `meta` element, whose `charset` attribute will be `charset_name`.

        Arguments:
            charset_name: The name of the character set the page is using,
                          the default value is `UTF-8`.
        """
        return cls(charset=charset_name)

    @classmethod
    def description(cls, desc: str) -> "meta":
        """
        Creates a description `meta` element.

        The `name` attribute of the created element will be `description` and
        its `content` attribute will be the `desc`.

        Arguments:
            desc: The short description of the page.
        """
        return cls(name="description", content=desc)

    @classmethod
    def keywords(cls, kwds: str) -> "meta":
        """
        Creates a keywords `meta` element.

        The `name` attribute of the created element will be `keywords` and
        its `content` attribute will be the `kwds`.

        Arguments:
            kwds: Keywords for search engines, comma separated list of words.
        """
        return cls(name="keywords", content=kwds)

    @classmethod
    def viewport(cls, spec: str = "width=device-width, initial-scale=1.0") -> "meta":
        """
        Creates a viewport `meta` element.

        The `name` attribute of the created element will be `viewport` and
        its `content` attribute will be the `spec`.

        Arguments:
            spec: The viewport settings to use, the default value is
                  `width=device-width, initial-scale=1.0`.
        """
        return cls(name="viewport", content=spec)


class script(StringElement):
    """
    `<script></script>` element.

    See https://www.w3schools.com/tags/tag_script.asp.
    """

    __slots__ = ()

    def __str__(self) -> str:
        if self.value:
            return f"<script {format_properties(self.properties)}>\n{self.value}\n</script>"
        else:
            return f"<script {format_properties(self.properties)}></script>"

    @classmethod
    def ref(cls, src: str) -> "script":
        """
        Creates a `script` element that references a JavaScript document instead of
        actually containing any JavaScript.

        Arguments:
            src: The location of the referenced script.
        """
        return cls("", src=src)


class style(StringElement):
    """
    `<style></style>` element.

    See https://www.w3schools.com/tags/tag_style.asp.
    """

    __slots__ = ()

    def __str__(self) -> str:
        value = self.value or ""
        return f"<style {format_properties(self.properties)}>\n{value}\n</style>"


def join(*args: Optional[str]) -> str:
    """
    Creates a string of space-separated entries from the given arguments.

    `None`s are automatically skipped.

    Typical use-case is to pass a set of CSS class names to this method to
    retrieve the final value of the `class` attribute of an element.
    """
    return " ".join(s for s in args if s is not None)


def webpage(*body_elements: ElementType,
            page_title: str,
            base_element: Optional[base] = None,
            class_: Optional[str] = None,
            metadata: Sequence[meta] = (),
            head_elements: Sequence[Union[link, script, style]] = (),
            javascript: Sequence[script] = (),
            **kwargs) -> ElementSequence:
    """
    Higher order component that composes a valid HTML page from the received arguments.

    The positional arguments of the method must be the elements that build up the
    actual webpage, i.e. the content to place inside the `<body></body>` HTML tag.

    The keyword arguments that are not listed in the arguments section will be set
    as attributes on the `body` element of the page.

    Arguments:
        page_title: The title of the webpage - mandatory keyword argument.
        base_element: The `base` element of the document that specifies the base URL/target
                      of relative URLs in the document.
        class_: CSS class names to set on the `body` element.
        metadata: The list of `meta` elements that describe the webpage.
        head_elements: Other elements that should be included in the head of the page
                       such as links, styles, and scripts.
        javascript: `script` elements that import JavaScript packages such as JQuery
                    or execute some JavaScript code.
    """
    return ElementSequence(
        DOCTYPE(),
        html(
            head(
                *[title(page_title), base_element] if base_element is not None else [title(page_title)],
                *metadata,
                *head_elements,
            ),
            body(
                *body_elements,
                *javascript,
                class_=class_,
                **kwargs
            )
        )
    )

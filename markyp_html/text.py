"""
HTML text elements (headings and paragraphs).
"""

from typing import Optional

from markyp import ElementType, PropertyValue
from markyp.elements import Element
from markyp_html import join


__all__ = ("TextElement", "h1", "h2", "h3", "h4", "h5", "h6", "p", "StyledTextFactory")


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


class StyledTextFactory(object):
    """
    Factory function for creating text elements with predefined CSS styles.
    """

    __slots__ = ("_base_css_class",)

    def __init__(self, base_css_class: str) -> None:
        """
        Initialization.

        Arguments:
            base_css_class: The CSS class name to set on created elements.
        """
        self._base_css_class: str = base_css_class

    @property
    def base_css_class(self) -> str:
        """
        The CSS class name to set on created elements.
        """
        return self._base_css_class

    def h1(self, *args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> TextElement:
        """
        Creates a `h1` element with `base_css_class` style.

        Positional arguments will become the children elements of the created element.

        Keyword arguments are turned into element attributes on the created element.

        Arguments:
            class_: Additional CSS class names to set on the created element.
        """
        return h1(*args, class_=join(self._base_css_class, class_), **kwargs)

    def h2(self, *args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> TextElement:
        """
        Creates a `h2` element with `base_css_class` style.

        Positional arguments will become the children elements of the created element.

        Keyword arguments are turned into element attributes on the created element.

        Arguments:
            class_: Additional CSS class names to set on the created element.
        """
        return h2(*args, class_=join(self._base_css_class, class_), **kwargs)

    def h3(self, *args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> TextElement:
        """
        Creates a `h3` element with `base_css_class` style.

        Positional arguments will become the children elements of the created element.

        Keyword arguments are turned into element attributes on the created element.

        Arguments:
            class_: Additional CSS class names to set on the created element.
        """
        return h3(*args, class_=join(self._base_css_class, class_), **kwargs)

    def h4(self, *args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> TextElement:
        """
        Creates a `h4` element with `base_css_class` style.

        Positional arguments will become the children elements of the created element.

        Keyword arguments are turned into element attributes on the created element.

        Arguments:
            class_: Additional CSS class names to set on the created element.
        """
        return h4(*args, class_=join(self._base_css_class, class_), **kwargs)

    def h5(self, *args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> TextElement:
        """
        Creates a `h5` element with `base_css_class` style.

        Positional arguments will become the children elements of the created element.

        Keyword arguments are turned into element attributes on the created element.

        Arguments:
            class_: Additional CSS class names to set on the created element.
        """
        return h5(*args, class_=join(self._base_css_class, class_), **kwargs)

    def h6(self, *args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> TextElement:
        """
        Creates a `h6` element with `base_css_class` style.

        Positional arguments will become the children elements of the created element.

        Keyword arguments are turned into element attributes on the created element.

        Arguments:
            class_: Additional CSS class names to set on the created element.
        """
        return h6(*args, class_=join(self._base_css_class, class_), **kwargs)

    def p(self, *args: ElementType, class_: Optional[str] = None, **kwargs: PropertyValue) -> TextElement:
        """
        Creates a `p` element with `base_css_class` style.

        Positional arguments will become the children elements of the created element.

        Keyword arguments are turned into element attributes on the created element.

        Arguments:
            class_: Additional CSS class names to set on the created element.
        """
        return p(*args, class_=join(self._base_css_class, class_), **kwargs)

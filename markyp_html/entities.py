"""
HTML entities.
"""

from markyp import IElement


__all__ = (
    "Entity",
    "amp",
    "apos",
    "cent",
    "copy",
    "euro",
    "gt",
    "lt",
    "mdash",
    "nbsp",
    "ndash",
    "pound",
    "quot",
    "reg",
    "times",
    "yen",
)


class Entity(IElement):
    """
    Class representing an HTML entity.
    """

    __slots__ = ("value",)

    def __init__(self, value: str) -> None:
        """
        """
        self.value: str = value
        """
        The string value of the HTML entity.
        """

    def __str__(self) -> str:
        return self.value


amp = Entity("&amp;")
"""
Ampersand entity.
"""

apos = Entity("&apos;")
"""
Single quotation mark (apostrophe) entity.
"""

cent = Entity("&cent;")
"""
Cent entity.
"""

copy = Entity("&copy;")
"""
Copyright entity.
"""

euro = Entity("&euro;")
"""
Euro entity.
"""

gt = Entity("&gt;")
"""
Greater than entity.
"""

lt = Entity("&lt;")
"""
Less than entity.
"""

mdash = Entity("&mdash;")
"""
Em dash entity.
"""

nbsp = Entity("&nbsp;")
"""
Non-breaking space entity.
"""

ndash = Entity("&ndash;")
"""
En dash entity.
"""

pound = Entity("&pound;")
"""
Pound entity.
"""

quot = Entity("&quot;")
"""
Double quotation mark entity.
"""

reg = Entity("&reg;")
"""
Registered trademark entity.
"""

times = Entity("&times;")
"""
Multiplication (X) entity.
"""

yen = Entity("&yen;")
"""
Yen entity.
"""

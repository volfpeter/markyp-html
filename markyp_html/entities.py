"""
HTML entities.
"""

from markyp import IElement


__all__ = (
    "Entity", "amp", "apos", "cent", "copy", "euro", "gt",
    "lt", "nbsp", "pound", "quot", "reg", "times", "yen"
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


amp: Entity = Entity("&amp;")
"""
Ampersand entity.
"""

apos: Entity = Entity("&apos;")
"""
Single quotation mark (apostrophe) entity.
"""

cent: Entity = Entity("&cent;")
"""
Cent entity.
"""

copy: Entity = Entity("&copy;")
"""
Copyright entity.
"""

euro: Entity = Entity("&euro;")
"""
Euro entity.
"""

gt: Entity = Entity("&gt;")
"""
Greater than entity.
"""

lt: Entity = Entity("&lt;")
"""
Less than entity.
"""

nbsp:Entity = Entity("&nbsp;")
"""
Non-breaking space entity.
"""

pound: Entity = Entity("&pound;")
"""
Pound entity.
"""

quot: Entity = Entity("&quot;")
"""
Double quotation mark entity.
"""

reg: Entity = Entity("&reg;")
"""
Registered trademark entity.
"""

times: Entity = Entity("&times;")
"""
Multiplication (X) entity.
"""

yen: Entity = Entity("&yen;")
"""
Yen entity.
"""

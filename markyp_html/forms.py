"""
HTML form elements.

See http://www.wikiwand.com/en/HTML_element#/Forms.
"""

from typing import Optional

from markyp import ElementType, PropertyValue
from markyp.elements import Element, StandaloneElement


__all__ = (
    "form", "button", "option", "optgroup", "datalist", "fieldset", "input_",
    "label", "legend", "meter", "output", "progress", "select", "textarea"
)


class form(Element):
    """
    `<form></form>` element.

    See https://www.w3schools.com/tags/tag_form.asp.
    """
    __slots__ = ()


class button(Element):
    """
    `<button></button>` element.

    See https://www.w3schools.com/tags/tag_button.asp.
    """

    __slots__ = ()

    @property
    def inline_children(self) -> bool:
        return True


class option(Element):
    """
    `<option></option>` element.

    See https://www.w3schools.com/tags/tag_option.asp.
    """

    __slots__ = ()

    @property
    def inline_children(self) -> bool:
        return True


class optgroup(Element):
    """
    `<optgroup></optgroup>` element.

    See https://www.w3schools.com/tags/tag_optgroup.asp.
    """

    __slots__ = ()

    def __init__(self, *args: option, class_: Optional[str] = None, **kwargs) -> None:
        super().__init__(*args, class_=class_, **kwargs)


class datalist(Element):
    """
    `<datalist></datalist>` element.

    See https://www.w3schools.com/tags/tag_datalist.asp.
    """

    __slots__ = ()

    def __init__(self, *args: option, class_: Optional[str] = None, **kwargs) -> None:
        super().__init__(*args, class_=class_, **kwargs)


class fieldset(Element):
    """
    `<fieldset></fieldset>` element.

    See https://www.w3schools.com/tags/tag_fieldset.asp.
    """
    __slots__ = ()


class input_(StandaloneElement):
    """
    `<input></input>` element.

    See https://www.w3schools.com/tags/tag_input.asp.
    """

    __slots__ = ()

    def __init__(self, *, class_: Optional[str] = None, type_: Optional[str] = None, **kwargs: PropertyValue) -> None:
        if type_ is not None:
            kwargs["type"] = type_
        super().__init__(class_=class_, **kwargs)

    @property
    def element_name(self) -> str:
        return "input"

    @classmethod
    def button(cls, class_: Optional[str] = None, **kwargs: PropertyValue) -> "input_":
        """
        Input element whose `type` is `button`.
        """
        return cls(class_=class_, type_="button", **kwargs)

    @classmethod
    def checkbox(cls, class_: Optional[str] = None, **kwargs: PropertyValue) -> "input_":
        """
        Input element whose `type` is `checkbox`.
        """
        return cls(class_=class_, type_="checkbox", **kwargs)

    @classmethod
    def email(cls, class_: Optional[str] = None, **kwargs: PropertyValue) -> "input_":
        """
        Input element whose `type` is `email`.
        """
        return cls(class_=class_, type_="email", **kwargs)

    @classmethod
    def file(cls, class_: Optional[str] = None, **kwargs: PropertyValue) -> "input_":
        """
        Input element whose `type` is `file`.
        """
        return cls(class_=class_, type_="file", **kwargs)

    @classmethod
    def hidden(cls, class_: Optional[str] = None, **kwargs: PropertyValue) -> "input_":
        """
        Input element whose `type` is `hidden`.
        """
        return cls(class_=class_, type_="hidden", **kwargs)

    @classmethod
    def number(cls, class_: Optional[str] = None, **kwargs: PropertyValue) -> "input_":
        """
        Input element whose `type` is `number`.
        """
        return cls(class_=class_, type_="number", **kwargs)

    @classmethod
    def password(cls, class_: Optional[str] = None, **kwargs: PropertyValue) -> "input_":
        """
        Input element whose `type` is `password`.
        """
        return cls(class_=class_, type_="password", **kwargs)

    @classmethod
    def radio(cls, class_: Optional[str] = None, **kwargs: PropertyValue) -> "input_":
        """
        Input element whose `type` is `radio`.
        """
        return cls(class_=class_, type_="radio", **kwargs)

    @classmethod
    def search(cls, class_: Optional[str] = None, **kwargs: PropertyValue) -> "input_":
        """
        Input element whose `type` is `search`.
        """
        return cls(class_=class_, type_="search", **kwargs)

    @classmethod
    def submit(cls, class_: Optional[str] = None, **kwargs: PropertyValue) -> "input_":
        """
        Input element whose `type` is `submit`.
        """
        return cls(class_=class_, type_="submit", **kwargs)

    @classmethod
    def text(cls, class_: Optional[str] = None, **kwargs: PropertyValue) -> "input_":
        """
        Input element whose `type` is `text`.
        """
        return cls(class_=class_, type_="text", **kwargs)

    @classmethod
    def time(cls, class_: Optional[str] = None, **kwargs: PropertyValue) -> "input_":
        """
        Input element whose `type` is `time`.
        """
        return cls(class_=class_, type_="time", **kwargs)


class label(Element):
    """
    `<label></label>` element.

    See https://www.w3schools.com/tags/tag_label.asp.
    """

    __slots__ = ()

    def __init__(self,
                 *args: ElementType,
                 class_: Optional[str] = None,
                 form_id: Optional[str] = None,
                 input_id: Optional[str] = None,
                 **kwargs: PropertyValue) -> None:
        if form_id is not None:
            kwargs["form"] = form_id
        if input_id is not None:
            kwargs["for"] = input_id
        super().__init__(*args, class_=class_, **kwargs)

    @property
    def inline_children(self) -> bool:
        return True


class legend(Element):
    """
    `<legend></legend>` element.

    See https://www.w3schools.com/tags/tag_legend.asp.
    """

    __slots__ = ()

    @property
    def inline_children(self) -> bool:
        return True


class meter(Element):
    """
    `<meter></meter>` element.

    See https://www.w3schools.com/tags/tag_meter.asp.
    """

    __slots__ = ()

    def __init__(self,
                 *args: ElementType,
                 value: float,
                 class_: Optional[str] = None,
                 **kwargs: PropertyValue) -> None:
        super().__init__(*args, value=value, class_=class_, **kwargs)

    @property
    def inline_children(self) -> bool:
        return True


class output(Element):
    """
    `<output></output>` element.

    See https://www.w3schools.com/tags/tag_output.asp.
    """
    __slots__ = ()


class progress(Element):
    """
    `<progress></progress>` element.

    See https://www.w3schools.com/tags/tag_progress.asp.
    """
    __slots__ = ()


class select(Element):
    """
    `<select></select>` element.

    See https://www.w3schools.com/tags/tag_select.asp.
    """

    __slots__ = ()

    def __init__(self, *args: option, class_: Optional[str] = None, **kwargs: PropertyValue) -> None:
        super().__init__(*args, class_=class_, **kwargs)


class textarea(Element):
    """
    `<textarea></textarea>` element.

    See https://www.w3schools.com/tags/tag_textarea.asp.
    """

    __slots__ = ()

[![Build Status](https://travis-ci.org/volfpeter/markyp-html.svg?branch=master)](https://travis-ci.org/volfpeter/markyp-html)
[![Downloads](https://pepy.tech/badge/markyp-html)](https://pepy.tech/project/markyp-html)
[![Downloads](https://pepy.tech/badge/markyp-html/month)](https://pepy.tech/project/markyp-html/month)
[![Downloads](https://pepy.tech/badge/markyp-html/week)](https://pepy.tech/project/markyp-html/week)

# markyp-html

[markyp](https://github.com/volfpeter/markyp)-based HTML implementations.

**Note**: if you're in an **async** environment, you should use [htmy](https://volfpeter.github.io/htmy/) instead! 

## Installation

The project is listed on the Python Package Index, it can be installed simply by executing `pip install markyp-html`.

## Getting started

If you are not familiar with the basic concepts of `markyp`, please start by having a look at its documentation [here](https://github.com/volfpeter/markyp).

The following very short example creates the most basic Hello World webpage. As you can see, all it takes is a single `webpage()` call and string conversion.

```Python
from markyp_html import webpage
page = webpage("Hello World!", page_title="Hello World")

# Get the actual HTML markup.
html = str(page)  # or page.markup
print(html)
```

Here is a slightly more sophisticated Hello World example, that contains all kinds of metadata, some CSS, and a couple of simple text elements:

```Python
from markyp_html import meta, style, webpage
from markyp_html.text import h1, p
from markyp_html.inline import strong

page = webpage(
    h1("markyp-html"),
    strong(p("Hello World!")),
    p("This page was generated using Python and markyp-html."),
    page_title="markyp-html demo page",
    head_elements=[style("h1 {color:red;}\np {color:blue;}")],
    metadata=[
        meta.author("Website Author"),
        meta.charset("UTF-8"),
        meta.description("markyp-html demo"),
        meta.keywords("markyp-html,markup,Python,HTML"),
        meta.viewport("width=device-width, initial-scale=1.0")
    ]
)

# Get the actual HTML markup.
html = str(page)  # or page.markup
print(html)
```

## `markyp-html` extensions

`markyp-html` is built on [markyp](https://github.com/volfpeter/markyp). In general, extensions follow the `markyp-{domain-or-extension-name}` naming convention.

Here is a list of extensions built on top of `markyp-html`:

- `markyp-bootstrap4`: Bootstrap 4 implementation at https://github.com/volfpeter/markyp-bootstrap4, contribution is welcome.
- `markyp-fontawesome`: Font Awesome icons for `markyp-html`-based web pages at https://github.com/volfpeter/markyp-fontawesome, contribution is welcome.
- `markyp-highlightjs`: Code highlighting in HTML using `highlight.js` at https://github.com/volfpeter/markyp-highlightjs, contribution is welcome.

If you have created an open source `markyp-html` extension, please let us know and we will include your project in this list.

## Community guidelines

In general, please treat each other with respect and follow the below guidelines to interact with the project:

- _Questions, feedback_: Open an issue with a `[Question] <issue-title>` title.
- _Bug reports_: Open an issue with a `[Bug] <issue-title>` title, an adequate description of the bug, and a code snippet that reproduces the issue if possible.
- _Feature requests and ideas_: Open an issue with an `[Enhancement] <issue-title>` title and a clear description of the enhancement proposal.

## Contribution guidelines

Every form of contribution is welcome, including documentation improvements, tests, bug fixes, and feature implementations.

Please follow these guidelines to contribute to the project:

- Make sure your changes match the documentation and coding style of the project, including [PEP 484](https://www.python.org/dev/peps/pep-0484/) type annotations.
- `mypy` is used to type-check the codebase, submitted code should not produce typing errors. See [this page](http://mypy-lang.org/) for more information on `mypy`.
- _Small_ fixes can be submitted simply by creating a pull request.
- Non-trivial changes should have an associated [issue](#community-guidelines) in the issue tracker that commits must reference (typically by adding `#refs <issue-id>` to the end of commit messages).
- Please write [tests](#testing) for the changes you make (if applicable).

If you have any questions about contributing to the project, please contact the project owner.

As mentioned in the [contribution guidelines](#contribution-guidelines), the project is type-checked using `mypy`, so first of all, the project must pass `mypy`'s static code analysis.

The project is tested using `pytest`. The chosen test layout is that tests are outside the application code, see [this page](https://docs.pytest.org/en/latest/goodpractices.html#tests-outside-application-code) for details on what it means in practice.

If `pytest` is installed, the test set can be executed using the `pytest test` command from within the project directory.

If `pytest-cov` is also installed, a test coverage report can be generated by executing `pytest test --cov markyp_html` from the root directory of the project.

## License - MIT

The library is open-sourced under the conditions of the MIT [license](https://choosealicense.com/licenses/mit/).

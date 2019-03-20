from codecs import open
from os import path
import re
from setuptools import setup, find_packages

# Get the long description from the README file
with open(path.join(path.abspath(path.dirname(__file__)), "README.md"), encoding="utf-8") as f:
    readme = f.read()

with open(path.join(path.abspath(path.dirname(__file__)), "src", "markyp_html", "__init__.py"), encoding="utf-8") as f:
    match = re.search("__version__ = \"(.*?)\"", f.read())
    version = match.group(1) if match else "0.0.0"

setup(
    name="markyp-html",
    version=version,
    description="HTML element implementations based on markyp.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/volfpeter/markyp-html",
    author="Peter Volf",
    author_email="do.volfp@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Utilities",
        "Typing :: Typed"
    ],
    keywords="html markup generator utility",
    package_dir={"": "src"},
    packages=find_packages("src", exclude=["test"]),
    python_requires=">=3.6",
    install_requires=[
        "markyp>=0.1903"
    ]
)

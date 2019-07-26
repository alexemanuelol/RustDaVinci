#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

NAME = "RustDaVinci"
VERSION = "0.1"
DESCRIPTION = "Automatic Sign Art Painter for the game Rust by Facepunch"
AUTHOR = "Alexander Emanuelsson"
EMAIL = "Alexander.Emanuelsson94@gmail.com"
URL = "https://github.com/alexemanuelol/RustDaVinci"
REQUIRED = [
    "Pillow>=5.4.1",
    "PyAutoGUI>=0.9.41",
    "pypiwin32>=223",
    "colorama>=0.4.1",
    "termcolor>=1.1.0",
    "pynput>=1.4.2"
]

with open("README.md") as file:
    readme = file.read()

with open("LICENSE.txt") as file:
    license = file.read()


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=readme,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    license=license,
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)"
    ]
)

import os

from setuptools import find_packages
from setuptools import setup

DATA_FILES = []
OPTIONS = {
    "argv_emulation": True,
    "iconfile": os.path.join("icons", "logo.jpg"),
    "plist": {
        "CFBundleIdentifier": "vinaydawani.What-is-Today",
        "CFBundleName": "What is Today",
        "CFBundleShortVersionString": "1.0",
        "CFBundleVersion": "1",
        "LSMinimumSystemVersion": "10.12",
        "LSUIElement": True,
    },
    "packages": ["rumps"],
}


setup(
    name="WhatisToday",
    version="1.0",
    app=["what_is_today/main.py"],
    data_files=DATA_FILES,
    author="Vinay Dawani",
    options={"py2app": OPTIONS},
    packages=find_packages(),
    setup_requires=[
        "py2app",
        "pyobjc-framework-CalendarStore",
        "pyobjc-framework-CoreWLAN",
        "pyobjc-framework-Quartz",
    ],
)
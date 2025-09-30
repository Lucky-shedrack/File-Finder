from setuptools import setup, find_packages

setup(
    name="file_search_cli",
    version="1.0.0",
    packages=find_packages(),
    py_modules=["main", "menus", "find", "settings", "terminal"],
    entry_points={
        "console_scripts": [
            "file-search=main:main",
        ],
    },
)

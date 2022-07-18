from setuptools import setup

setup(
    name="mkdocs-nedoc-plugin",
    version="0.0.1",
    description="Nedoc plugin for linking to API documentation",
    author="Jakub Beránek",
    author_email="berykubik@gmail.com",
    url="https://github.com/kobzol/mkdocs-nedoc-plugin",
    packages=["mkdocs_nedoc_plugin"],
    entry_points={
        'mkdocs.plugins': [
            'nedoc = mkdocs_nedoc_plugin:NedocPlugin',
        ]
    }
)

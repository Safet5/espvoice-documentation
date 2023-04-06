# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'ESPVoice'
copyright = '2023, ST5'
author = 'The ESPVoice Team'

version = '1.0.0'
release = version

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.spelling',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_logo = "_static/espvoice_logo-100x100.png"
html_favicon = "_static/favicon.ico"
# -- Options for EPUB output
epub_show_urls = 'footnote'

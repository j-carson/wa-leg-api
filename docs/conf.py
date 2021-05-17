# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../wa_leg_api'))


# -- Project information -----------------------------------------------------

project = 'wa_leg_api'
copyright = '2021, Janet Carson'
author = 'Janet Carson'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'myst_parser'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.ipynb_checkpoints', '.git']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'agogo'
html_theme_options = {
    
#    bodyfont (CSS font family): Font for normal text.
    'bodyfont' : 'sans-serif',
    
#    headerfont (CSS font family): Font for headings.
#    pagewidth (CSS length): Width of the page content, default 70em.
#    documentwidth (CSS length): Width of the document (without sidebar), default 50em.
#    sidebarwidth (CSS length): Width of the sidebar, default 20em.
#    rightsidebar (true or false): Put the sidebar on the right side. Defaults to True.
    'rightsidebar' : False,
    
#    bgcolor (CSS color): Background color.
    'bgcolor' : 'rgba(200, 200, 200, .2)',
    
#    headerbg (CSS value for “background”): background for the header area, default a grayish gradient.
    'headerbg': 'rgb(45, 134, 45)',
    
#    footerbg (CSS value for “background”): background for the footer area, default a light gray gradient.
    
#    linkcolor (CSS color): Body link color.
    'linkcolor' : 'rgba(0, 82, 204, 0.8)',
    
#    headercolor1, headercolor2 (CSS color): colors for <h1> and <h2> headings.
    'headercolor1' : 'rgba(82, 0, 204, 1.0)',
    'headercolor2' : 'rgba(82, 0, 204, 0.7)',
    
#    headerlinkcolor (CSS color): Color for the backreference link in headings.
    'headerlinkcolor' : 'rgba(255, 170, 0, 1.0)',
    
#    textalign (CSS text-align value): Text alignment for the body, default is justify.
    'textalign' : 'left',
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Extension configuration -------------------------------------------------

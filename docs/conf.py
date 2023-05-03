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

from textdescriptives.about import __version__

# -- Project information -----------------------------------------------------

project = "textdescriptives"
author = "Lasse Hansen, Kenneth Enevoldsen"

# The full version, including alpha/beta/rc tags
release = __version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinxext.opengraph",
    "sphinx_copybutton",
    "sphinx.ext.githubpages",
    "sphinxcontrib.autodoc_pydantic",
    "myst_nb",
    "IPython.sphinxext.ipython_console_highlighting",
    "sphinx_design",
]

# autodoc_mock_imports = ["textdescriptives"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]

# Autodoc Pydantic
autodoc_pydantic_model_show_json = False
autodoc_pydantic_model_show_config = False
autodoc_pydantic_model_show_field_summary = False


# -- Options for myst-nb -----------------------------------------------------

# set the timeout for executing notebooks
# nb_execution_timeout = 600  # in seconds, default 30 seconds
nb_execution_timeout = 600  # in seconds, default 30 seconds. 600 seconds = 10 minutes

# always fail CI pipeline when nb cannot be executed
nb_execution_raise_on_error = True


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_show_sourcelink = True

source_suffix = {".rst": "restructuredtext", ".md": "myst-nb", ".ipynb": "myst-nb"}

html_context = {
    "display_github": True,  # Add 'Edit on Github' link instead of 'View page source'
    "github_user": "HLasse",
    "github_repo": project,
    "github_version": "main",
    "conf_py_path": "/docs/",
}

html_theme_options = {
    "light_logo": "icon.png",
    "dark_logo": "icon_dark.png",
    "light_css_variables": {
        "color-brand-primary": "#ff5454",
        "color-brand-content": "#ff7575",
    },
    "dark_css_variables": {
        "color-brand-primary": "#ff8f8f",
        "color-brand-content": "#ff8f8f",
    },
    "sidebar_hide_name": True,
    "navigation_with_keys": True,
}

# pygments_style = "monokai"
# pygments_dark_style = "monokai"

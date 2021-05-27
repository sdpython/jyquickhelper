
.. |gitlogo| image:: _static/git_logo.png
             :height: 20

.. image:: https://github.com/sdpython/jyquickhelper/blob/master/_doc/sphinxdoc/source/phdoc_static/project_ico.png?raw=true
    :target: https://github.com/sdpython/jyquickhelper/

jyquickhelper: javascript extensions for notebooks
==================================================

.. image:: https://travis-ci.com/sdpython/jyquickhelper.svg?branch=master
    :target: https://travis-ci.com/sdpython/jyquickhelper
    :alt: Build status

.. image:: https://ci.appveyor.com/api/projects/status/2tyc3or7snm6w4xl?svg=true
    :target: https://ci.appveyor.com/project/sdpython/jyquickhelper
    :alt: Build Status Windows

.. image:: https://circleci.com/gh/sdpython/jyquickhelper/tree/master.svg?style=svg
    :target: https://circleci.com/gh/sdpython/jyquickhelper/tree/master

.. image:: https://badge.fury.io/py/jyquickhelper.svg
    :target: http://badge.fury.io/py/jyquickhelper

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :alt: MIT License
    :target: http://opensource.org/licenses/MIT

.. image:: https://requires.io/github/sdpython/jyquickhelper/requirements.svg?branch=master
     :target: https://requires.io/github/sdpython/jyquickhelper/requirements/?branch=master
     :alt: Requirements Status

.. image:: https://codecov.io/github/sdpython/jyquickhelper/coverage.svg?branch=master
    :target: https://codecov.io/github/sdpython/jyquickhelper?branch=master

.. image:: http://img.shields.io/github/issues/sdpython/jyquickhelper.png
    :alt: GitHub Issues
    :target: https://github.com/sdpython/jyquickhelper/issues

.. image:: nbcov.png
    :target: http://www.xavierdupre.fr/app/jyquickhelper/helpsphinx/all_notebooks_coverage.html
    :alt: Notebook Coverage

.. image:: https://pepy.tech/badge/jyquickhelper
    :target: https://pypi.org/project/jyquickhelper/
    :alt: Downloads

.. image:: https://img.shields.io/github/forks/sdpython/jyquickhelper.svg
    :target: https://github.com/sdpython/jyquickhelper/
    :alt: Forks

.. image:: https://img.shields.io/github/stars/sdpython/jyquickhelper.svg
    :target: https://github.com/sdpython/jyquickhelper/
    :alt: Stars

.. image:: https://img.shields.io/github/repo-size/sdpython/jyquickhelper
    :target: https://github.com/sdpython/jyquickhelper/
    :alt: size

Helpers for Jupyter notebooks, implements javascript additions
such a menu, wraps a json viewer, a graphviz viewer.

.. toctree::
    :maxdepth: 1

    api/index
    i_index
    i_ex
    all_notebooks
    index_modules
    blog/blogindex

.. exref::
    :title: Add a Javascript menu to a notebook

    ::

        from jyquickheler import add_menu_notebook
        add_menu_notebook()

    See :ref:`notebookhtmlsvgrst`.

.. exref::
    :title: Render Javascript in a notebook

    ::

        from jyquickhelper import RenderJS
        css = ["https://cdnjs.cloudflare.com/ajax/libs/c3/0.4.21/c3.min.css"]
        RenderJS(script, css=css, libs = [
                        dict(path="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.17/d3.min.js",
                             name="d3", exports="d3"),
                        dict(path="https://cdnjs.cloudflare.com/ajax/libs/c3/0.4.21/c3.min.js",
                             name="c3", exports="c3", deps=["d3"])])

    See :ref:`nbc3rst` or :ref:`nbmermaidrst`.

.. exref::
    :title: Visualize JSON in a notebook.

    ::

        from jyquickhelper import JSONJS
        JSONJS(dict(name="xavier", city="Paris"), html_only=True, show_to_level=3)

    See :ref:`nbjsonrst`.

.. image:: https://mybinder.org/badge_logo.svg
    :target: https://mybinder.org/v2/gh/sdpython/jyquickhelper/master?filepath=_doc%2Fnotebooks
    :alt: Binder

**Links:** `github <https://github.com/sdpython/jyquickhelper/>`_,
`documentation <http://www.xavierdupre.fr/app/jyquickhelper/helpsphinx/index.html>`_,
:ref:`l-README`,
:ref:`blog <ap-main-0>`,
:ref:`l-issues-todolist`

+----------------------+---------------------+---------------------+--------------------+------------------------+------------------------------------------------+
| :ref:`l-modules`     |  :ref:`l-functions` | :ref:`l-classes`    | :ref:`l-methods`   | :ref:`l-staticmethods` | :ref:`l-properties`                            |
+----------------------+---------------------+---------------------+--------------------+------------------------+------------------------------------------------+
| :ref:`modindex`      |  :ref:`l-EX2`       | :ref:`search`       | :ref:`l-license`   | :ref:`l-changes`       | :ref:`l-README`                                |
+----------------------+---------------------+---------------------+--------------------+------------------------+------------------------------------------------+
| :ref:`genindex`      |  :ref:`l-FAQ2`      | :ref:`l-notebooks`  |                    | :ref:`l-statcode`      | `Unit Test Coverage <coverage/index.html>`_    |
+----------------------+---------------------+---------------------+--------------------+------------------------+------------------------------------------------+

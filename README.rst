
.. image:: https://github.com/sdpython/jyquickhelper/blob/master/_doc/sphinxdoc/source/_static/project_ico.png?raw=true
    :target: https://github.com/sdpython/jyquickhelper/

.. _l-README:

jyquickhelper: javascript extensions for notebooks
==================================================

.. image:: https://travis-ci.com/sdpython/jyquickhelper.svg?branch=master
    :target: https://app.travis-ci.com/github/sdpython/jyquickhelper
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

.. image:: https://codecov.io/github/sdpython/jyquickhelper/coverage.svg?branch=master
    :target: https://codecov.io/github/sdpython/jyquickhelper?branch=master

.. image:: http://img.shields.io/github/issues/sdpython/jyquickhelper.png
    :alt: GitHub Issues
    :target: https://github.com/sdpython/jyquickhelper/issues

.. image:: http://www.xavierdupre.fr/app/jyquickhelper/helpsphinx/_images/nbcov.png
    :target: http://www.xavierdupre.fr/app/jyquickhelper/helpsphinx/all_notebooks_coverage.html
    :alt: Notebook Coverage

.. image:: https://pepy.tech/badge/jyquickhelper/month
    :target: https://pepy.tech/project/jyquickhelper/month
    :alt: Downloads

.. image:: https://img.shields.io/github/forks/sdpython/jyquickhelper.svg
    :target: https://github.com/sdpython/jyquickhelper/
    :alt: Forks

.. image:: https://img.shields.io/github/stars/sdpython/jyquickhelper.svg
    :target: https://github.com/sdpython/jyquickhelper/
    :alt: Stars

.. image:: https://mybinder.org/badge_logo.svg
    :target: https://mybinder.org/v2/gh/sdpython/jyquickhelper/master?filepath=_doc%2Fnotebooks
    :alt: Binder

.. image:: https://img.shields.io/github/repo-size/sdpython/jyquickhelper
    :target: https://github.com/sdpython/jyquickhelper/
    :alt: size

Helpers for Jupyter notebooks.
Example to run from a notebook:

::

    from jyquickheler import add_menu_notebook
    add_menu_notebook()

A menu is displayed:

* first section of level 2
* section section of level 2
* ...

It helps rendering javascript:

::

    from jyquickhelper import RenderJS
    css = ["https://cdnjs.cloudflare.com/ajax/libs/c3/0.4.21/c3.min.css"]
    RenderJS(script, css=css, libs = [
                    dict(path="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.17/d3.min.js",
                         name="d3", exports="d3"),
                    dict(path="https://cdnjs.cloudflare.com/ajax/libs/c3/0.4.21/c3.min.js",
                         name="c3", exports="c3", deps=["d3"])])

See `c3.ipynb <http://www.xavierdupre.fr/app/jyquickhelper/helpsphinx/notebooks/nb_c3.html>`_.
Or visualizing JSON:

::

    from jyquickhelper import JSONJS
    JSONJS(dict(name="xavier", city="Paris"), html_only=True, show_to_level=3)

See `nb_json.ipynb <http://www.xavierdupre.fr/app/jyquickhelper/helpsphinx/notebooks/nb_json.html>`_.

**Links:**

* `GitHub/jyquickhelper <https://github.com/sdpython/jyquickhelper/>`_
* `documentation <http://www.xavierdupre.fr/app/jyquickhelper/helpsphinx/index.html>`_
* `Blog <http://www.xavierdupre.fr/app/jyquickhelper/helpsphinx/blog/main_0000.html#ap-main-0>`_

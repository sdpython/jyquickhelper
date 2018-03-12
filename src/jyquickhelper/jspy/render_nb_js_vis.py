# -*- coding: utf-8 -*-
"""
@file
@brief Renders a network in Javascript.
"""
import os
from .render_nb_js import RenderJS


class RenderJsVis(RenderJS):
    """
    Renders a network in a :epkg:`notebook`
    with :epkg:`vis.js`.
    """

    def __init__(self, js, local=False, width="100%", height="100%", divid=None,
                 style=None, only_html=True, div_class=None, check_urls=True,
                 class_vis='Netwwork'):
        """
        @param  js              (str) javascript
        @param  local           (bool) use local path to javascript dependencies
        @param  script          (str) script
        @param  width           (str) width
        @param  height          (str) height
        @param  style           (str) style (added in ``<style>...</style>``)
        @param  divid           (str|None) id of the div
        @param  only_html       (bool) use only function `display_html <http://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html?highlight=display_html#IPython.display.display_html>`_
                                and not `display_javascript <http://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html?highlight=display_html#IPython.display.display_javascript>`_ to add
                                javascript to the page.
        @param  div_class       (str) class of the section ``div`` which will host the results
                                of the javascript
        @param  check_urls      (bool) by default, check url exists
        @param  class_vis       (str) visualization class (*Network*, *Timeline*, ...)

        The script must defined variables *options* and *data* if
        ``class_vis=='Network'``.
        """
        script = RenderJsVis._build_script(js)
        libs, css = RenderJsVis._get_libs_css(local)
        RenderJS.__init__(self, script, width=width, height=height, divid=divid,
                          only_html=only_html, div_class=div_class, check_urls=True,
                          libs=libs, css=css, local=local)

    @staticmethod
    def _get_libs_css(local):
        """
        Returns the dependencies.

        @param      local       use local file (True) or remote urls (False)
        @param      lite        use lite version
        @return                 tuple *(libs, css)*
        """
        libs = [  # 'vis-timeline-graph2d.min.js',
            #'vis-network.min.js',
            #'vis-graph3d.min.js',
            'vis.min.js']
        css = ['vis-timeline-graph2d.min.css',
               'vis-network.min.css',
               'vis.min.css']

        if local:
            this = os.path.dirname(__file__)
            libs = [dict(path=os.path.join(this, '..', 'js',
                                           'visjs', j), name=j.split('.')[0]) for j in libs]
            css = [os.path.join(this, '..', 'js', 'visjs', j) for j in css]
        else:
            libs = [dict(path='http://www.xavierdupre.fr/js/visjs/' +
                         j, name=j.split('.')[0]) for j in libs]
            css = ['http://www.xavierdupre.fr/js/visjs/' + j for j in css]
        return libs, css

    @staticmethod
    def _build_script(js):
        """
        Builds the javascript script.

        @param      js      javascript
        @return             javascript
        """
        script = js + "\nvar container = document.getElementById('__ID__');" + \
            "\nvar network = new vis.Network(container, data, options);\n"
        return script

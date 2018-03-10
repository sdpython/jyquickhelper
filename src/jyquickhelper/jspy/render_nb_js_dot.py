# -*- coding: utf-8 -*-
"""
@file
@brief Renders a graph in Javascript.
"""

from .render_nb_js import RenderJS


class RenderJsDot(RenderJS):
    """
    Renders a graph in a :epkg:`notebook`
    defined in :epkg:`DOT` language
    with :epkg:`viz.js`.
    """

    def __init__(self, dot, local=False, width="100%", height="100%", divid=None,
                 style=None, only_html=True, div_class=None, check_urls=True):
        """
        @param  dot             (str) dot
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
        """
        script = RenderJsDot._build_script(dot)
        libs, css = RenderJsDot._get_libs_css(local)
        RenderJS.__init__(self, script, width=width, height=height, divid=divid,
                          only_html=only_html, div_class=div_class, check_urls=True,
                          libs=libs, css=css)

    @staticmethod
    def _get_libs_css(local):
        """
        Returns the dependencies.

        @return         tuple *(libs, css)*
        """
        if local:
            raise NotImplementedError('Local path is not implemented yet')
        libs = ['http://www.xavierdupre.fr/js/vizjs/viz-lite.js']
        css = None
        return libs, css

    @staticmethod
    def _build_script(dot):
        """
        Builds the javascript script based wrapping the
        :epkg:`DOT` language.

        @param      dot     :epkg:`DOT` language
        @return             javscript script
        """
        dot = dot.replace('"', '\\"').replace('\n', '\\n')
        script = """var svgGraph = Viz("{0}");\ndocument.getElementById('__ID__').innerHTML = svgGraph;""".format(
            dot)
        return script

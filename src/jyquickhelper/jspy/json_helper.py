# -*- coding: utf-8 -*-
"""
@file
@brief Helpers around JSON
"""
import uuid
import json
from IPython.display import display_html, display_javascript


class RenderJSONRaw(object):
    """
    Renders :epkg:`JSON` using :epkg:`javascript`.
    """

    def __init__(self, json_data, width="100%", height="100%", divid=None, show_to_level=None):
        """
        Initialize with a :epkg:`JSON` data.

        @param  json_data       dictionary or string
        @param  width           (str) width
        @param  height          (str) height
        @param  divid           (str|None) id of the div
        @param  show_to_level   (int|None) show first level
        """
        if isinstance(json_data, (dict, list)):
            self.json_str = json.dumps(json_data)
        else:
            self.json_str = json
        self.uuid = divid if divid else str(uuid.uuid4())
        self.width = width
        self.height = height
        self.show_to_level = show_to_level

    def generate_html(self):
        """
        Overloads method
        `_ipython_display_ <http://ipython.readthedocs.io/en/stable/config/integrating.html?highlight=Integrating%20>`_.
        """
        level = " show_to_level={}".format(
            self.show_to_level) if self.show_to_level is not None else ''
        ht = '<div id="{}" style="height: {}; width:{};"{}></div>'.format(
            self.uuid, self.width, self.height, level)
        js = """
        require(["https://rawgit.com/caldwell/renderjson/master/renderjson.js"], function() {
        document.getElementById('%s').appendChild(renderjson(%s))
        }); """ % (self.uuid, self.json_str)
        return ht, js


class RenderJSONObj(RenderJSONRaw):
    """
    Renders :epkg:`JSON` using :epkg:`javascript`.
    """

    def _ipython_display_(self):
        ht, js = self.generate_html()
        display_html(ht, raw=True)
        display_javascript(js, raw=True)


class RenderJSON(RenderJSONRaw):
    """
    Renders :epkg:`JSON` using :epkg:`javascript`, outputs only :epkg:`HTML`.
    """

    def _repr_html_(self):
        ht, js = self.generate_html()
        ht += "\n<script>\n{0}\n</script>\n".format(js)
        return ht


def JSONJS(data, html_only=True, show_to_level=None):
    """
    Inspired from `Pretty JSON Formatting in IPython Notebook <http://stackoverflow.com/questions/18873066/pretty-json-formatting-in-ipython-notebook>`_.

    @param      data            dictionary or json string
    @param      show_to_level   show first level
    @return                     @see cl RenderJSON

    The function uses librairy
    `renderjson <https://github.com/caldwell/renderjson>`_.
    It returns an object with overwrite method
    `_ipython_display_ <http://ipython.readthedocs.io/en/stable/config/integrating.html?highlight=Integrating%20>`_.

    .. faqref::
        :title: Persistent javascript in a conververted notebook

        After a couple of tries, it appears that it is more efficient to
        render the javascript inside a section ``<script>...</script>``
        when the notebook is converted to RST (*html_only=True*).
    """
    if html_only:
        return RenderJSON(data, show_to_level=show_to_level)
    else:
        return RenderJSONObj(data, show_to_level=show_to_level)

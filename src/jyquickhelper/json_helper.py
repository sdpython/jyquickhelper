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
    render JSON using javascript
    """

    def __init__(self, json_data, width="100%", height="100%", divid=None):
        """
        initialize with a JSON data

        @param  json_data       dictionary or string
        @param  width           (str) width
        @param  height          (str) height
        @param  divid           (str|None) id of the div
        """
        if isinstance(json_data, (dict, list)):
            self.json_str = json.dumps(json_data)
        else:
            self.json_str = json
        self.uuid = divid if divid else str(uuid.uuid4())
        self.width = width
        self.height = height

    def generate_html(self):
        """
        overloads method
        `_ipython_display_ <http://ipython.readthedocs.io/en/stable/config/integrating.html?highlight=Integrating%20>`_.
        """
        ht = '<div id="{}" style="height: {}; width:{};"></div>'.format(
            self.uuid, self.width, self.height)
        js = """
        require(["https://rawgit.com/caldwell/renderjson/master/renderjson.js"], function() {
        document.getElementById('%s').appendChild(renderjson(%s))
        }); """ % (self.uuid, self.json_str)
        return ht, js


class RenderJSONObj(RenderJSONRaw):
    """
    render JSON using javascript
    """

    def _ipython_display_(self):
        ht, js = self.generate_html()
        display_html(ht, raw=True)
        display_javascript(js, raw=True)


class RenderJSON(RenderJSONRaw):
    """
    render JSON using javascript, outputs only HTML
    """

    def _repr_html_(self):
        ht, js = self.generate_html()
        ht += "\n<script>\n{0}\n</script>\n".format(js)
        return ht


def JSONJS(data, html_only=True):
    """
    Inspired from `Pretty JSON Formatting in IPython Notebook <http://stackoverflow.com/questions/18873066/pretty-json-formatting-in-ipython-notebook>`_.

    @param      data       dictionary or json string
    @return                @see cl RenderJSON

    The function uses librairy
    `renderjson <https://github.com/caldwell/renderjson>`_.
    It returns an object with overwrite method
    `_ipython_display_ <http://ipython.readthedocs.io/en/stable/config/integrating.html?highlight=Integrating%20>`_.

    .. faqref::
        :title: Persistent javascript in a conververted notebook

        After a couple of tries, it appears that it is more efficient to
        render the javascript inside a section ``<script>...</script>``
        when the notebook is converted to RST.
    """
    if html_only:
        return RenderJSON(data)
    else:
        return RenderJSONObj(data)

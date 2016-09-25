# -*- coding: utf-8 -*-
"""
@file
@brief Helpers around JSON
"""
import uuid
import json
from IPython.display import display_html, display_javascript


class RenderJSON(object):
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
        if isinstance(json_data, dict):
            self.json_str = json.dumps(json_data)
        else:
            self.json_str = json
        self.uuid = divid if divid else str(uuid.uuid4())
        self.width = width
        self.height = height

    def _ipython_display_(self):
        """
        overloads method
        `_ipython_display_ <http://ipython.readthedocs.io/en/stable/config/integrating.html?highlight=Integrating%20>`_.
        """
        display_html('<div id="{}" style="height: {}; width:{};"></div>'.format(self.uuid, self.width, self.height),
                     raw=True)
        display_javascript("""
        require(["https://rawgit.com/caldwell/renderjson/master/renderjson.js"], function() {
        document.getElementById('%s').appendChild(renderjson(%s))
        }); """ % (self.uuid, self.json_str), raw=True)


def JSONJS(data):
    """
    Inspired from `Pretty JSON Formatting in IPython Notebook <http://stackoverflow.com/questions/18873066/pretty-json-formatting-in-ipython-notebook>`_.

    @param      data       dictionary or json string
    @return                @see cl RenderJSON

    The function uses librairy
    `renderjson <https://github.com/caldwell/renderjson>`_.
    It returns an object with overwrite method
    `_ipython_display_ <http://ipython.readthedocs.io/en/stable/config/integrating.html?highlight=Integrating%20>`_.
    """
    return RenderJSON(data)

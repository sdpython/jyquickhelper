# -*- coding: utf-8 -*-
"""
@file
@brief Helpers around JSON
"""
import uuid
from IPython.display import display_html, display_javascript


class RenderJS(object):
    """
    render JS using javascript
    """

    def __init__(self, script, width="100%", height="100%", divid=None, css=None, libs=None):
        """
        initialize with a JS script

        @param  script          (str) script
        @param  width           (str) width
        @param  height          (str) height
        @param  divid           (str|None) id of the div
        @param  css             (list) list of css
        @param  libs            (list) list of dependencies
        """
        self.script = script
        self.uuid = divid if divid else str(uuid.uuid4())
        self.width = width
        self.height = height
        self.libs = libs
        self.css = css
        if "__ID__" not in script:
            raise ValueError(
                "The sript does not contain any string __ID__. It is replaced by the ID value in script:\n{0}".format(script))

    def _ipython_display_(self):
        """
        overloads method
        `_ipython_display_ <http://ipython.readthedocs.io/en/stable/config/integrating.html?highlight=Integrating%20>`_.
        """
        if self.css:
            css = "".join(
                '<link rel="stylesheet" href="{0}" type="text/css" />'.format(c) for c in self.css)
            ht = '<div id="{0}-css">{3}<div id="{0}" style="height: {1}; width:{2};"></div></div>'.format(self.uuid,
                                                                                                          self.width, self.height, css)
        else:
            css = ""
            ht = '<div id="{0}" style="height: {1}; width:{2};"></div>'.format(self.uuid,
                                                                               self.width, self.height)
        display_html(ht, raw=True)
        if self.libs:
            require = ",".join('"{0}"'.format(l) for l in self.libs)
        else:
            require = ""
        script = self.script.replace("__ID__", self.uuid)
        if self.libs:
            js = """require([%s], function() { %s }); """ % (require, script)
        else:
            js = script
        display_javascript(js, raw=True)

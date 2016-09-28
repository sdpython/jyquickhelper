# -*- coding: utf-8 -*-
"""
@file
@brief Helpers around JSON
"""
import uuid
from IPython.display import display_html, display_javascript


class RenderJSRaw(object):
    """
    render JS using javascript
    """

    def __init__(self, script, width="100%", height="100%", divid=None, css=None,
                 libs=None, style=None, only_html=False, div_class=None):
        """
        initialize with a JS script

        @param  script          (str) script
        @param  width           (str) width
        @param  height          (str) height
        @param  style           (str) style (added in ``<style>...</style>``)
        @param  divid           (str|None) id of the div
        @param  css             (list) list of css
        @param  libs            (list) list of dependencies
        @param  only_html       (bool) use only function `display_html <http://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html?highlight=display_html#IPython.display.display_html>`_
                                and not `display_javascript <http://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html?highlight=display_html#IPython.display.display_javascript>`_ to add
                                javascript to the page.
        @param  div_class       (str) class of the section ``div`` which will host the results
                                of the javascript
        """
        self.script = script
        self.uuid = divid if divid else "M" + \
            str(uuid.uuid4()).replace("-", "")
        self.width = width
        self.height = height
        self.libs = libs
        self.css = css
        self.style = style
        self.only_html = only_html
        self.div_class = div_class
        if "__ID__" not in script:
            raise ValueError(
                "The sript does not contain any string __ID__. It is replaced by the ID value in script:\n{0}".format(script))

    def generate_html(self):
        """
        overloads method
        `_ipython_display_ <http://ipython.readthedocs.io/en/stable/config/integrating.html?highlight=Integrating%20>`_.

        @return     HTML text, Javascript text
        """
        if self.style:
            style = "<style>{0}</style>".format(self.style)
        else:
            style = ""
        if self.div_class:
            divcl = ' class="{0}"'.format(self.div_class)
        else:
            divcl = ""
        dims = ""
        if self.height:
            dims += "height:{0};".format(self.height)
        if self.width:
            dims += "width:{0};".format(self.width)
        if len(dims) > 0:
            dims = ' style="{0}"'.format(dims)
        if self.css:
            css = "".join(
                '<link rel="stylesheet" href="{0}" type="text/css" />'.format(c) for c in self.css)
            ht = '<div id="{0}-css">{2}{3}<div{4} id="{0}"{1}></div></div>'.format(self.uuid,
                                                                                   dims, css, style, divcl)
        else:
            css = ""
            ht = '<div id="{0}-cont"{1}>{2}<div{3} id="{0}"></div></div>'.format(
                self.uuid, dims, style, divcl)

        script = self.script.replace("__ID__", self.uuid)
        if self.libs:
            names = []
            paths = []
            shims = {}
            args = []
            exports = []
            for l in self.libs:
                if isinstance(l, dict):
                    name = l.get("name", None)
                    if "path" in l:
                        p = l["path"]
                        if name is None:
                            name = ".".join((p.split("/")[-1]).split(".")[:-1])
                        path = ".".join(p.split(".")[:-1])
                        paths.append((name, path))
                    else:
                        raise KeyError(
                            "unable to find 'path' in {0}".format(l))
                    names.append(name)
                    args.append(name)
                    if "exports" in l:
                        if name not in shims:
                            shims[name] = {}
                        shims[name]["exports"] = l["exports"]
                        if isinstance(l["exports"], list):
                            exports.extend(l["exports"])
                        else:
                            exports.append(l["exports"])
                    if "deps" in l:
                        if name not in shims:
                            shims[name] = {}
                        shims[name]["deps"] = l["deps"]
                else:
                    names.append(l)
            if len(names) == 0:
                raise ValueError("names is empty.\nlibs={0}\npaths={1}\nshims={2}\nexports={3}".format(self.libs,
                                                                                                       paths, shims, exports))
            require = ",".join("'{0}'".format(l) for l in names)

            config = ["require.config({"]
            if len(paths) > 0:
                config.append("paths:{")
                for name, path in paths:
                    config.append("'{0}':'{1}',".format(name, path))
                config.append("},")
            if len(shims) > 0:
                config.append("shim:{")

                def vd(d):
                    rows = []
                    for k, v in sorted(d.items()):
                        rows.append("'{0}':{1}".format(
                            k, v if isinstance(v, list) else "'{0}'".format(v)))
                    return "{%s}" % ",".join(rows)
                for k, v in sorted(shims.items()):
                    config.append("'{0}':{1},".format(k, vd(v)))
                config.append("},")
            config.append("});")
            if len(config) > 2:
                prefix = "\n".join(config) + "\n"
            else:
                prefix = ""
            js = prefix + \
                """\nrequire([%s], function(%s) { %s });\n""" % (
                    require, ",".join(args), script)
        else:
            js = script
        if self.only_html:
            ht += "\n<script>\n%s\n</script>" % js
            return ht, None
        else:
            return ht, js


class RenderJSObj(RenderJSRaw):
    """
    render JS using javascript
    """

    def _ipython_display_(self):
        """
        overloads method
        `_ipython_display_ <http://ipython.readthedocs.io/en/stable/config/integrating.html?highlight=Integrating%20>`_.
        """
        ht, js = self.generate_html()
        if js is None:
            display_html(ht, raw=True)
        else:
            display_html(ht, raw=True)
            display_javascript(js, raw=True)


class RenderJS(RenderJSRaw):
    """
    render JS using javascript, only outputs HTML
    """

    def _repr_html_(self):
        """
        overloads method *_repr_html_*
        """
        ht, js = self.generate_html()
        ht += "\n<script>\n{0}\n</script>\n".format(js)
        return ht

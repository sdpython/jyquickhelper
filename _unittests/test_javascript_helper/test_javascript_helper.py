"""
@brief      test log(time=2s)
"""

import sys
import os
import unittest


try:
    import src
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src

try:
    import pyquickhelper as skip_
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyquickhelper",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pyquickhelper as skip_

from pyquickhelper.loghelper import fLOG
from src.jyquickhelper import RenderJS
from src.jyquickhelper.javascript_helper import RenderJSObj


class TestJavascriptHelper(unittest.TestCase):

    def test_javascript_helper(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        try:
            f = RenderJSObj("", css=["_css"], libs=["_libs"])
        except ValueError:
            pass
        f = RenderJSObj("__ID__", css=["_css"], libs=["_libs"])
        assert f
        f._ipython_display_()

        f = RenderJSObj("__ID__", css=None, libs=["_libs"])
        assert f
        f._ipython_display_()

        f = RenderJSObj("__ID__", css=None, libs=None)
        assert f
        f._ipython_display_()

        f = RenderJSObj("__ID__", css=["_css"], libs=None)
        assert f
        f._ipython_display_()

        f = RenderJSObj("__ID__", css=["_css"], libs=["_libs"], style="r")
        assert f
        f._ipython_display_()

        f = RenderJSObj("__ID__", css=["_css"], libs=[
            "_libs"], style="r", width=None, height=None)
        assert f
        f._ipython_display_()

        f = RenderJS("__ID__", css=["_css"], libs=[
                     "_libs"], style="r", width=None, height=None)
        assert f
        f._repr_html_()

    def test_javascript_helper_config(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        script = """
         var chart = c3.generate({
            bindto: '#__ID__',
            data: {
              columns: [
                ['data1', 30, 200, 100, 400, 150, 250],
                ['data2', 50, 20, 10, 40, 15, 25]
              ]
            }
        });
        """
        f = RenderJS(script, divid="MYID", css=["http://c3js.org/css/c3.css"],
                     libs=[dict(name="d3", path="http://d3js.org/d3.v3.min.js", exports="d3"),
                           dict(name="c3", path="http://c3js.org/js/c3.min-4c5bef8f.js", exports="c3", deps=["d3"])])
        assert f
        ht, js = f.generate_html()
        assert ht
        assert js
        exp = """<div id="MYID-css"><link rel="stylesheet" href="http://c3js.org/css/c3.css" type="text/css" />""" + \
              """<div id="MYID" style="height:100%;width:100%;"></div></div>"""
        assert exp in ht
        exp = """
            require.config({
            paths:{
            'd3':'http://d3js.org/d3.v3.min',
            'c3':'http://c3js.org/js/c3.min-4c5bef8f',
            },
            shim:{
            'c3':{'deps':['d3'],'exports':'c3'},
            'd3':{'exports':'d3'},
            },
            });

            require(['d3','c3'],function(d3,c3){
            varchart=c3.generate({
            bindto:'#MYID',
            data:{
            columns:[
            ['data1',30,200,100,400,150,250],
            ['data2',50,20,10,40,15,25]
            ]
            }
            });
            });
        """.replace(" ", "").replace("\r", "").strip("\n ")
        js = js.replace(" ", "").replace("\r", "").strip("\n ").replace("u'", "'")
        self.maxDiff = None
        # fLOG(js)
        self.assertEqual(js, exp)


if __name__ == "__main__":
    unittest.main()

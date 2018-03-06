"""
@brief      test log(time=2s)
"""

import sys
import os
import unittest

try:
    from io import StringIO
    from contextlib import redirect_stdout
    testoutput = True
except ImportError:
    testoutput = False


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
from pyquickhelper.pycode import skipif_circleci
from src.jyquickhelper import RenderJS
from src.jyquickhelper.jspy.javascript_helper import RenderJSObj


class TestJavascriptHelper(unittest.TestCase):

    @skipif_circleci('output is empty, probably already captured, should be investigated')
    def test_javascript_helper(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        try:
            f = RenderJSObj("", css=["_css"], libs=["_libs"])
        except ValueError:
            pass
        f = RenderJSObj("__ID__", css=["_css"],
                        libs=["_libs"], check_urls=False)
        if testoutput:
            st = StringIO()
            with redirect_stdout(st):
                f._ipython_display_()
            self.assertIn("{'text/html': '<div id=", st.getvalue())

        f = RenderJSObj("__ID__", css=None, libs=["_libs"], check_urls=False)
        if testoutput:
            st = StringIO()
            with redirect_stdout(st):
                f._ipython_display_()
            self.assertIn("{'text/html': '<div id=", st.getvalue())

        f = RenderJSObj("__ID__", css=None, libs=None, check_urls=False)
        if testoutput:
            st = StringIO()
            with redirect_stdout(st):
                f._ipython_display_()
            self.assertIn("{'text/html': '<div id=", st.getvalue())

        f = RenderJSObj("__ID__", css=["_css"], libs=None, check_urls=False)
        if testoutput:
            st = StringIO()
            with redirect_stdout(st):
                f._ipython_display_()
            self.assertIn("{'text/html': '<div id=", st.getvalue())

        f = RenderJSObj("__ID__", css=["_css"], libs=[
                        "_libs"], style="r", check_urls=False)
        if testoutput:
            st = StringIO()
            with redirect_stdout(st):
                f._ipython_display_()
            self.assertIn("{'text/html': '<div id=", st.getvalue())

        f = RenderJSObj("__ID__", css=["_css"], libs=[
            "_libs"], style="r", width=None, height=None, check_urls=False)
        if testoutput:
            st = StringIO()
            with redirect_stdout(st):
                f._ipython_display_()
            self.assertIn("{'text/html': '<div id=", st.getvalue())

        f = RenderJS("__ID__", css=["_css"], libs=[
                     "_libs"], style="r", width=None, height=None, check_urls=False)
        res = f._repr_html_()
        self.assertIn("require(['_libs'], function() {", res)

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
        f = RenderJS(script, divid="MYID", css=["https://cdnjs.cloudflare.com/ajax/libs/c3/0.4.21/c3.min.css"],
                     libs=[dict(name="d3", path="https://cdnjs.cloudflare.com/ajax/libs/d3/4.13.0/d3.min.js", exports="d3"),
                           dict(name="c3", path="https://cdnjs.cloudflare.com/ajax/libs/c3/0.4.21/c3.min.js",
                                exports="c3", deps=["d3"])])
        assert f
        ht, js = f.generate_html()
        assert ht
        assert js
        exp = """<div id="MYID-css"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/c3/0.4.21/c3.min.css" type="text/css" />""" + \
              """<div id="MYID" style="height:100%;width:100%;"></div></div>"""

        self.assertIn(exp, ht)
        exp = """
            require.config({
            paths:{
            'd3':'https://cdnjs.cloudflare.com/ajax/libs/d3/4.13.0/d3.min',
            'c3':'https://cdnjs.cloudflare.com/ajax/libs/c3/0.4.21/c3.min',
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
        js = js.replace(" ", "").replace(
            "\r", "").strip("\n ").replace("u'", "'")
        self.maxDiff = None
        # fLOG(js)
        self.assertEqual(js, exp)


if __name__ == "__main__":
    unittest.main()

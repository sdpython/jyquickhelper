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
from src.jyquickhelper import RenderJsVis


class TestRenderNbJsVis(unittest.TestCase):

    script = """
      var nodes = new vis.DataSet([
        {id: 1, label: 'Node 1'},
        {id: 2, label: 'Node 2'},
        {id: 3, label: 'Node 3'},
        {id: 4, label: 'Node 4'},
        {id: 5, label: 'Node 5'}
      ]);

      // create an array with edges
      var edges = new vis.DataSet([
        {from: 1, to: 3},
        {from: 1, to: 2},
        {from: 2, to: 4},
        {from: 2, to: 5},
        {from: 3, to: 3}
      ]);

      // create a network
      var data = {
        nodes: nodes,
        edges: edges
      };
      var options = {};
      """

    def test_render_nb_js_vis_dot(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        f = RenderJsVis(dot="digraph{ a -> b; }")
        assert f
        if hasattr(f, "_ipython_display_"):
            f._ipython_display_()
        else:
            f._repr_html_()

        f = RenderJsVis(dot="digraph{ a -> b; }", only_html=True)
        out = f._repr_html_()
        self.assertIn('var network = new vis.Network(', out)
        self.assertNotIn('None', out)

    def test_render_nb_js_vis_dot_options(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        f = RenderJsVis(dot="digraph{ a -> b; }")
        assert f
        if hasattr(f, "_ipython_display_"):
            f._ipython_display_()
        else:
            f._repr_html_()

        f = RenderJsVis(dot="digraph{ a -> b; }",
                        only_html=True, layout='hierarchical')
        out = f._repr_html_()
        self.assertIn('var network = new vis.Network(', out)
        self.assertIn('var options = {layout:{', out)
        self.assertNotIn('None', out)

    def test_render_nb_js_vis(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        f = RenderJsVis(TestRenderNbJsVis.script)
        assert f
        if hasattr(f, "_ipython_display_"):
            f._ipython_display_()
        else:
            f._repr_html_()

        f = RenderJsVis(TestRenderNbJsVis.script, only_html=True)
        out = f._repr_html_()
        self.assertIn('var network = new vis.Network(', out)
        self.assertNotIn('None', out)

    def test_render_nb_js_vis_api(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        f = RenderJsVis(TestRenderNbJsVis.script, only_html=True)
        out = f._repr_html_()
        self.assertIn('var network = new vis.Network(', out)
        self.assertNotIn('None', out)

    def test_render_nb_js_vis_local(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        f = RenderJsVis(TestRenderNbJsVis.script)
        assert f
        if hasattr(f, "_ipython_display_"):
            f._ipython_display_()
        else:
            f._repr_html_()

        f = RenderJsVis(TestRenderNbJsVis.script, only_html=True, local=True)
        out = f._repr_html_()
        self.assertIn('var network = new vis.Network(', out)
        self.assertNotIn('None', out)

    def test_render_nb_js_vis_api_local(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        f = RenderJsVis(TestRenderNbJsVis.script, only_html=True, local=True)
        out = f._repr_html_()
        self.assertIn('var network = new vis.Network(', out)
        self.assertNotIn('None', out)

    def test_render_nb_js_vis_exc(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.assertRaises(ValueError, lambda: RenderJsVis(
            only_html=True, local=True))
        self.assertRaises(ValueError, lambda: RenderJsVis(
            'jj', only_html=True, local=True))
        self.assertRaises(ValueError, lambda: RenderJsVis(
            '__ID__', only_html=True, local=True))
        self.assertRaises(ValueError, lambda: RenderJsVis(
            '__ID__', only_html=True, local=True, class_vis='r'))


if __name__ == "__main__":
    unittest.main()

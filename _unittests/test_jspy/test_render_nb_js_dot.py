"""
@brief      test log(time=2s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from jyquickhelper import RenderJsDot


class TestRenderNbJsDot(unittest.TestCase):

    def test_render_nb_js_dot(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        f = RenderJsDot(dot='digraph{ a -> b; }')
        assert f
        if hasattr(f, "_ipython_display_"):
            f._ipython_display_()
        else:
            f._repr_html_()

        f = RenderJsDot(dot='digraph{ a -> b; }', only_html=True)
        out = f._repr_html_()
        self.assertIn('var svgGraph = Viz("', out)
        self.assertNotIn('None', out)

    def test_render_nb_js_dot_api(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        f = RenderJsDot(dot='digraph{ a -> b; }', only_html=True)
        out = f._repr_html_()
        self.assertIn('var svgGraph = Viz("', out)
        self.assertNotIn('None', out)

    def test_render_nb_js_dot_local(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        f = RenderJsDot(dot='digraph{ a -> b; }')
        assert f
        if hasattr(f, "_ipython_display_"):
            f._ipython_display_()
        else:
            f._repr_html_()

        f = RenderJsDot(dot='digraph{ a -> b; }', only_html=True, local=True)
        out = f._repr_html_()
        self.assertIn('var svgGraph = Viz("', out)
        self.assertNotIn('None', out)

    def test_render_nb_js_dot_api_local(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        f = RenderJsDot(dot='digraph{ a -> b; }', only_html=True, local=True)
        out = f._repr_html_()
        self.assertIn('var svgGraph = Viz("', out)
        self.assertNotIn('None', out)


if __name__ == "__main__":
    unittest.main()

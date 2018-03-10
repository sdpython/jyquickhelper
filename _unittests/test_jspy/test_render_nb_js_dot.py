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
from src.jyquickhelper import RenderJsDot


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


if __name__ == "__main__":
    unittest.main()

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
from src.jyquickhelper import JSONJS


class TestRenderNbJson(unittest.TestCase):

    def test_render_nb_json(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        f = JSONJS(dict(a="a"))
        assert f
        if hasattr(f, "_ipython_display_"):
            f._ipython_display_()
        else:
            f._repr_html_()

        f = JSONJS(dict(a="a"), only_html=True)
        assert f
        r = f._repr_html_()
        self.assertIn('require(["https', r)

    def test_render_nb_json_api(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        import requests
        data_json = requests.get(
            "http://api.worldbank.org/countries?incomeLevel=LMC&format=json").json()
        f = JSONJS(data_json, only_html=True)
        assert f
        r = f._repr_html_()
        self.assertIn('require(["https', r)

    def test_render_nb_json_local(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        f = JSONJS(dict(a="a"), local=True)
        assert f
        if hasattr(f, "_ipython_display_"):
            f._ipython_display_()
        else:
            f._repr_html_()

        f = JSONJS(dict(a="a"), only_html=True, local=True)
        assert f
        r = f._repr_html_()
        self.assertIn('require(["renderjson.js"]', r)

    def test_render_nb_json_api_local(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        import requests
        data_json = requests.get(
            "http://api.worldbank.org/countries?incomeLevel=LMC&format=json").json()
        f = JSONJS(data_json, only_html=True, local=True)
        assert f
        r = f._repr_html_()
        self.assertIn('require(["renderjson.js"]', r)


if __name__ == "__main__":
    unittest.main()
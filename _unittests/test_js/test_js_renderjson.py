"""
@brief      test log(time=2s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG


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

from src.jyquickhelper.js import load_extension


class TestJsRenderJson(unittest.TestCase):

    def test_js_render_json(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        ext = load_extension('renderjson', kind='str')
        self.assertIn("require(['renderjson", ext)
        self.assertIn('document.getElementsByTagName', ext)
        self.assertIn('load_jyq_css_renderjson', ext)
        self.assertIn("load_jyq_css_renderjson('renderjson", ext)


if __name__ == "__main__":
    unittest.main()

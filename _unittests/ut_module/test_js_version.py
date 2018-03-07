"""
@brief      test log(time=0s)
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
                "src",)))
    if path not in sys.path:
        sys.path.append(path)
    import pyquickhelper as skip_

from pyquickhelper.loghelper import fLOG
from src.jyquickhelper.js.c3 import version as vc3
from src.jyquickhelper.js.d3 import version as vd3
from src.jyquickhelper.js.eve import version as vexe
from src.jyquickhelper.js.raphael import version as vraph
from src.jyquickhelper.js.treant import version as vtr
from src.jyquickhelper.js.custom import version as vc
from src.jyquickhelper.js.renderjson import version as vjs
from src.jyquickhelper.js.mermaid import version as vme
from src.jyquickhelper.js.vizjs import version as vjz


class TestJsVersion(unittest.TestCase):

    def test_js_version(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        for f in [vc3, vd3, vexe, vraph, vtr, vc, vjs, vme, vjz]:
            spl = f().split('.')
            self.assertGreater(len(spl), 1)


if __name__ == "__main__":
    unittest.main()

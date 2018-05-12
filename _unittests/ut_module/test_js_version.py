"""
@brief      test log(time=0s)
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


from src.jyquickhelper.js.c3 import version as vc3
from src.jyquickhelper.js.d3 import version as vd3
from src.jyquickhelper.js.eve import version as vexe
from src.jyquickhelper.js.raphael import version as vraph
from src.jyquickhelper.js.treant import version as vtr
from src.jyquickhelper.js.custom import version as vc
from src.jyquickhelper.js.renderjson import version as vjs
from src.jyquickhelper.js.mermaid import version as vme
from src.jyquickhelper.js.vizjs import version as vjz
from src.jyquickhelper.js.visjs import version as vjs2
from src.jyquickhelper.js.svgpanzoom import version as vspz
from src.jyquickhelper.js.svg import version as vsvg
from src.jyquickhelper.js.cytoscape import version as vcyt
from src.jyquickhelper.js.pig import version as vpig


class TestJsVersion(unittest.TestCase):

    def test_js_version(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        root = os.path.join(os.path.dirname(src.__file__), "jyquickhelper")
        for i, f in enumerate([vc3, vd3, vexe, vraph, vtr, vc, vjs,
                               vme, vjz, vspz, vsvg, vjs2, vcyt, vpig]):
            spl = f().split('.')
            self.assertGreater(len(spl), 1)
            name = f.__module__.split('jyquickhelper')[-1].strip('.')
            fold = os.path.join(root, *name.split("."))
            js = [_ for _ in os.listdir(
                fold) if os.path.splitext(_)[-1] == '.js']
            if len(js) == 0:
                raise FileNotFoundError(
                    "({2}) No js found for '{0}' in '{1}'.".format(name, fold, i))
            if 'custom' in name:
                continue
            lic = [_ for _ in os.listdir(fold) if 'LICENSE' in _]
            if len(lic) == 0:
                raise FileNotFoundError(
                    "({2}) No license found for '{0}' in '{1}'.".format(name, fold, i))


if __name__ == "__main__":
    unittest.main()

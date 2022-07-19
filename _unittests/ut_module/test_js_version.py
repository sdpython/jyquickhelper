"""
@brief      test log(time=0s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
import jyquickhelper
from jyquickhelper.js.c3 import version as vc3
from jyquickhelper.js.d3 import version as vd3
from jyquickhelper.js.eve import version as vexe
from jyquickhelper.js.raphael import version as vraph
from jyquickhelper.js.treant import version as vtr
from jyquickhelper.js.custom import version as vc
from jyquickhelper.js.renderjson import version as vjs
from jyquickhelper.js.mermaid import version as vme
from jyquickhelper.js.vizjs import version as vjz
from jyquickhelper.js.visjs import version as vjs2
from jyquickhelper.js.svgpanzoom import version as vspz
from jyquickhelper.js.svg import version as vsvg
from jyquickhelper.js.cytoscape import version as vcyt
from jyquickhelper.js.pig import version as vpig


class TestJsVersion(unittest.TestCase):

    def test_js_version(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        root = os.path.dirname(jyquickhelper.__file__)
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
                    f"({i}) No js found for '{name}' in '{fold}'.")
            if 'custom' in name:
                continue
            lic = [_ for _ in os.listdir(fold) if 'LICENSE' in _]
            if len(lic) == 0:
                raise FileNotFoundError(
                    f"({i}) No license found for '{name}' in '{fold}'.")


if __name__ == "__main__":
    unittest.main()

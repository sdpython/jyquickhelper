# -*- coding: utf-8 -*-
"""
@brief      test log(time=5s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, skipif_appveyor
from pyquickhelper.ipythonhelper import execute_notebook_list, execute_notebook_list_finalize_ut

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

import src.jyquickhelper


class TestRunNotebooksPythonVisjs(unittest.TestCase):

    @unittest.skipIf(sys.version_info[0] == 2, "notebook only working with python 3")
    @skipif_appveyor("Fails on appveyor")
    def test_run_notebook(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_run_notebooks_visjs")

        fnb = os.path.normpath(os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "..", "..", "_doc", "notebooks"))
        keepnote = []
        for f in os.listdir(fnb):
            if os.path.splitext(f)[-1] == ".ipynb" and "visjs" in f:
                keepnote.append(os.path.join(fnb, f))
        for i, f in enumerate(keepnote):
            fLOG(i + 1, os.path.split(f)[-1])

        addpaths = [os.path.normpath(os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "..", "..", "src"))]

        res = execute_notebook_list(
            temp, keepnote, fLOG=fLOG, additional_path=addpaths)
        execute_notebook_list_finalize_ut(
            res, fLOG=fLOG, dump=src.jyquickhelper)


if __name__ == "__main__":
    unittest.main()
# -*- coding: utf-8 -*-
"""
@brief      test log(time=11s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
from pyquickhelper.ipythonhelper import execute_notebook_list, execute_notebook_list_finalize_ut
import jyquickhelper


class TestRunNotebooksPythonCustoJs(unittest.TestCase):

    @unittest.skipIf(sys.version_info[0] == 2, "notebook only working with python 3")
    def test_run_notebook(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_run_notebooks_custom_js")

        fnb = os.path.normpath(os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "..", "..", "_doc", "notebooks"))
        keepnote = []
        for f in os.listdir(fnb):
            if os.path.splitext(f)[-1] == ".ipynb" and "_long" not in f and \
                "js" in f and \
                    ("custom" in f or "local" in f):
                keepnote.append(os.path.join(fnb, f))
        for i, f in enumerate(keepnote):
            fLOG(i + 1, os.path.split(f)[-1])

        addpaths = [os.path.normpath(os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "..", "..", "src"))]

        # run the notebooks
        res = execute_notebook_list(
            temp, keepnote, fLOG=fLOG, additional_path=addpaths)
        execute_notebook_list_finalize_ut(
            res, fLOG=fLOG, dump=jyquickhelper)


if __name__ == "__main__":
    unittest.main()

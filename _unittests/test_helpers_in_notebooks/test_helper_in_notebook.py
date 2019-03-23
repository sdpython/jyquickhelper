"""
@brief      test log(time=2s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from jyquickhelper import set_notebook_name_theNotebook, add_notebook_menu


class TestHelperInNotebook(unittest.TestCase):

    def test_store_notebook_path(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        r = set_notebook_name_theNotebook(display=False)
        assert r is not None

    def test_add_notebook_menu(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        r = add_notebook_menu()
        assert r is not None
        r = add_notebook_menu(format="rst")
        assert r is not None


if __name__ == "__main__":
    unittest.main()

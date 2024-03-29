"""
@brief      test log(time=0s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import check_pep8, ExtTestCase


class TestCodeStyle(ExtTestCase):
    """Test style."""

    def test_style_src(self):
        thi = os.path.abspath(os.path.dirname(__file__))
        src_ = os.path.normpath(os.path.join(thi, "..", "..", "src"))
        check_pep8(src_, fLOG=fLOG,
                   pylint_ignore=('C0103', 'C1801', 'R1705', 'W0108', 'W0613',
                                  'C0111', "W0212", 'C0415', 'C0209', 'W0107',
                                  'C3001', 'R1735'),
                   skip=["Unable to import 'urllib2'",
                         "Redefining built-in 'format'",
                         "R1720",
                         ])

    def test_style_test(self):
        thi = os.path.abspath(os.path.dirname(__file__))
        test = os.path.normpath(os.path.join(thi, "..", ))
        check_pep8(test, fLOG=fLOG, neg_pattern="temp_.*",
                   pylint_ignore=('C0103', 'C1801', 'R1705', 'W0108', 'W0613',
                                  'C0111', "W0212", 'C0415', 'C0209', 'W0107',
                                  'C3001', 'R1735'),
                   skip=["Instance of 'RenderJsVis' has no '_ipython_display_'",
                         "Instance of 'RenderJsDot' has no '_ipython_display_'",
                         "R1720",
                         ])


if __name__ == "__main__":
    unittest.main()

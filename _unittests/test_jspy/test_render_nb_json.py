"""
@brief      test log(time=2s)
"""
import unittest
from jyquickhelper import JSONJS


class TestRenderNbJson(unittest.TestCase):

    def test_render_nb_json(self):
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
        import requests  # pylint: disable=C0415
        data_json = requests.get(
            "http://api.worldbank.org/countries?incomeLevel=LMC&format=json").json()
        f = JSONJS(data_json, only_html=True)
        assert f
        r = f._repr_html_()
        self.assertIn('require(["https', r)

    def test_render_nb_json_local(self):
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
        import requests  # pylint: disable=C0415
        data_json = requests.get(
            "http://api.worldbank.org/countries?incomeLevel=LMC&format=json",
            timeout=5).json()
        f = JSONJS(data_json, only_html=True, local=True)
        assert f
        r = f._repr_html_()
        self.assertIn('require(["renderjson.js"]', r)


if __name__ == "__main__":
    unittest.main(verbosity=2)

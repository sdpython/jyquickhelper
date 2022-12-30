# -*- coding: utf-8 -*-
import sys
import os
import alabaster
from pyquickhelper.helpgen.default_conf import set_sphinx_variables

sys.path.insert(0, os.path.abspath(os.path.join(os.path.split(__file__)[0])))

local_template = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), "phdoc_templates")

set_sphinx_variables(__file__, "jyquickhelper", "Xavier Dupré", 2021,
                     "alabaster", alabaster.get_path(),
                     locals(), extlinks=dict(issue=(
                         'https://github.com/sdpython/jyquickhelper/issues/%s',
                         'issue %s')),
                     title="jyquickhelper", book=True)

blog_root = "http://www.xavierdupre.fr/app/jyquickhelper/helpsphinx/"
html_css_files = ['my-styles.css']
html_logo = "phdoc_static/project_ico.png"
html_sidebars = {}

language = "en"
custom_preamble = """\n
\\newcommand{\\vecteur}[2]{\\pa{#1,\\dots,#2}}
\\newcommand{\\N}[0]{\\mathbb{N}}
\\newcommand{\\indicatrice}[1]{\\mathbf{1\\!\\!1}_{\\acc{#1}}}
\\usepackage[all]{xy}
\\newcommand{\\infegal}[0]{\\leqslant}
\\newcommand{\\supegal}[0]{\\geqslant}
\\newcommand{\\ensemble}[2]{\\acc{#1,\\dots,#2}}
\\newcommand{\\fleche}[1]{\\overrightarrow{ #1 }}
\\newcommand{\\intervalle}[2]{\\left\\{#1,\\cdots,#2\\right\\}}
\\newcommand{\\loinormale}[2]{{\\cal N}\\pa{#1,#2}}
\\newcommand{\\independant}[0]{\\;\\makebox[3ex]{\\makebox[0ex]{\\rule[-0.2ex]{3ex}{.1ex}}\\!\\!\\!\\!\\makebox[.5ex][l]{\\rule[-.2ex]{.1ex}{2ex}}\\makebox[.5ex][l]{\\rule[-.2ex]{.1ex}{2ex}}} \\,\\,}
\\newcommand{\\esp}{\\mathbb{E}}
\\newcommand{\\var}{\\mathbb{V}}
\\newcommand{\\pr}[1]{\\mathbb{P}\\pa{#1}}
\\newcommand{\\loi}[0]{{\\cal L}}
\\newcommand{\\vecteurno}[2]{#1,\\dots,#2}
\\newcommand{\\norm}[1]{\\left\\Vert#1\\right\\Vert}
\\newcommand{\\dans}[0]{\\rightarrow}
\\newcommand{\\partialfrac}[2]{\\frac{\\partial #1}{\\partial #2}}
\\newcommand{\\partialdfrac}[2]{\\dfrac{\\partial #1}{\\partial #2}}
\\newcommand{\\loimultinomiale}[1]{{\\cal M}\\pa{#1}}
\\newcommand{\\trace}[1]{tr\\pa{#1}}
\\newcommand{\\abs}[1]{\\left|#1\\right|}
"""
# \\usepackage{eepic}

imgmath_latex_preamble += custom_preamble
latex_elements['preamble'] += custom_preamble
mathdef_link_only = True

# references
epkg_dictionary['DOT'] = 'https://en.wikipedia.org/wiki/DOT_(graph_description_language)'
epkg_dictionary['eve'] = 'http://evejs.com/'
epkg_dictionary['HTML'] = 'https://en.wikipedia.org/wiki/HTML'
epkg_dictionary['javascript'] = 'https://en.wikipedia.org/wiki/JavaScript'
epkg_dictionary['JSON'] = 'https://en.wikipedia.org/wiki/JSON'
epkg_dictionary['notebook'] = 'http://jupyter.org/'
epkg_dictionary['raphael'] = 'http://dmitrybaranovskiy.github.io/raphael/'
epkg_dictionary['renderjson'] = 'https://github.com/caldwell/renderjson'
epkg_dictionary['RST'] = 'https://en.wikipedia.org/wiki/RST'
epkg_dictionary['viz.js'] = 'https://github.com/mdaines/viz.js/'

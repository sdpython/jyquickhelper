# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
import os
from setuptools import setup, find_packages
from pyquicksetup import read_version, read_readme, default_cmdclass


#########
# settings
#########

project_var_name = "jyquickhelper"
versionPython = "%s.%s" % (sys.version_info.major, sys.version_info.minor)
path = "Lib/site-packages/" + project_var_name
readme = 'README.rst'
history = "HISTORY.rst"
requirements = None

KEYWORDS = project_var_name + ', Xavier Dupré'
DESCRIPTION = """Helpers for Jupyter notebooks: automated menu, JSON visualizer, plug javascript"""
CLASSIFIERS = [
    'Programming Language :: Python :: 3',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering',
    'Topic :: Education',
    'License :: OSI Approved :: MIT License',
    'Development Status :: 5 - Production/Stable'
]

#######
# data
#######

packages = find_packages('src', exclude='src')
package_dir = {k: "src/" + k.replace(".", "/") for k in packages}
package_data = {
    project_var_name + ".js.renderjson": ["*.js", "*.css", "*.txt"],
    project_var_name + ".js.visjs": ["*.js", "*.css", "*.txt"],
    project_var_name + ".js.vizjs": ["*.js", "*.css", "*.txt"],
}

setup(
    name=project_var_name,
    version=read_version(__file__, project_var_name, subfolder='src'),
    author='Xavier Dupré',
    author_email='xavier.dupre@gmail.com',
    license="MIT",
    url="http://www.xavierdupre.fr/app/jyquickhelper/helpsphinx/index.html",
    download_url="https://github.com/sdpython/jyquickhelper/",
    description=DESCRIPTION,
    long_description=read_readme(__file__),
    cmdclass=default_cmdclass(),
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
    packages=packages,
    package_dir=package_dir,
    package_data=package_data,
    setup_requires=['pyquicksetup>=0.2'],
    install_requires=['ipython', 'jupyter', 'notebook'],
)

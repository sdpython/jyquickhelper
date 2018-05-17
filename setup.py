# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
import os
from distutils.core import setup
from setuptools import find_packages

#########
# settings
#########

project_var_name = "jyquickhelper"
sversion = "0.3"
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

############
# functions
############


def is_local():
    file = os.path.abspath(__file__).replace("\\", "/").lower()
    if "/temp/" in file and "pip-" in file:
        return False
    for cname in {"bdist_msi", "build27", "build_script", "build_sphinx", "build_ext",
                  "bdist_wheel", "bdist_egg", "bdist_wininst", "clean_pyd", "clean_space",
                  "copy27", "copy_dist", "local_pypi", "notebook", "publish", "publish_doc",
                  "register", "unittests", "unittests_LONG", "unittests_SKIP", "unittests_GUI",
                  "run27", "sdist", "setupdep", "test_local_pypi", "upload_docs", "setup_hook",
                  "copy_sphinx", "write_version", "lab", "history", 'run_pylint'}:
        if cname in sys.argv:
            return True
    else:
        return False

    return False


def ask_help():
    return "--help" in sys.argv or "--help-commands" in sys.argv


def verbose():
    print("---------------------------------")
    print("package_dir =", package_dir)
    print("packages    =", packages)
    print("package_data=", package_data)
    print("current     =", os.path.abspath(os.getcwd()))
    print("---------------------------------")

##########
# version
##########


if is_local() and not ask_help():
    def write_version():
        from pyquickhelper.pycode import write_version_for_setup
        return write_version_for_setup(__file__)

    write_version()

    versiontxt = os.path.join(os.path.dirname(__file__), "version.txt")
    if os.path.exists(versiontxt):
        with open(versiontxt, "r") as f:
            lines = f.readlines()
        subversion = "." + lines[0].strip("\r\n ")
        if subversion == ".0":
            raise Exception("Git version is wrong: '{0}'.".format(subversion))
    else:
        raise FileNotFoundError(versiontxt)
else:
    # when the module is installed, no commit number is displayed
    subversion = ""

if "upload" in sys.argv and not subversion and not ask_help():
    # avoid uploading with a wrong subversion number
    raise Exception(
        "Git version is empty, cannot upload, is_local()={0}".format(is_local()))

##############
# common part
##############

if os.path.exists(readme):
    with open(readme, "r", encoding='utf-8-sig') as f:
        long_description = f.read()
else:
    long_description = ""
if os.path.exists(history):
    with open(history, "r", encoding='utf-8-sig') as f:
        long_description += f.read()

if "--verbose" in sys.argv:
    verbose()

if is_local():
    import pyquickhelper
    logging_function = pyquickhelper.get_fLOG()
    from pyquickhelper.pycode import process_standard_options_for_setup
    logging_function(OutputPrint=True)
    r = process_standard_options_for_setup(
        sys.argv, __file__, project_var_name,
        unittest_modules=["pyquickhelper"],
        additional_notebook_path=["pyquickhelper",
                                  "pymyinstall", "jyquickhelper"],
        additional_local_path=["pyquickhelper",
                               "pymyinstall", "jyquickhelper"],
        requirements=["pyquickhelper", "pymyinstall", "jyquickhelper"],
        layout=["html"], github_owner="sdpython",
        add_htmlhelp=sys.platform.startswith("win"),
        coverage_options=dict(omit=["*exclude*.py"]),
        fLOG=logging_function, covtoken=("24e81424-08ba-4ca7-be23-66c12926565f ", "'_UT_36_std' in outfile"))
    if not r and not ({"bdist_msi", "sdist",
                       "bdist_wheel", "publish", "publish_doc", "register",
                       "upload_docs", "bdist_wininst", "build_ext"} & set(sys.argv)):
        raise Exception("unable to interpret command line: " + str(sys.argv))
else:
    r = False

if ask_help():
    from pyquickhelper.pycode import process_standard_options_for_setup_help
    process_standard_options_for_setup_help(sys.argv)

if not r:
    if len(sys.argv) in (1, 2) and sys.argv[-1] in ("--help-commands",):
        from pyquickhelper.pycode import process_standard_options_for_setup_help
        process_standard_options_for_setup_help(sys.argv)
    from pyquickhelper.pycode import clean_readme
    long_description = clean_readme(long_description)
    setup(
        name=project_var_name,
        version='%s%s' % (sversion, subversion),
        author='Xavier Dupré',
        author_email='xavier.dupre@gmail.com',
        license="MIT",
        url="http://www.xavierdupre.fr/app/jyquickhelper/helpsphinx/index.html",
        download_url="https://github.com/sdpython/jyquickhelper/",
        description=DESCRIPTION,
        long_description=long_description,
        keywords=KEYWORDS,
        classifiers=CLASSIFIERS,
        packages=packages,
        package_dir=package_dir,
        package_data=package_data,
        install_requires=['ipython', 'jupyter', 'notebook'],
    )

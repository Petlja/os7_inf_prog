import os
import sys
import paver
from paver.easy import options, Bunch
import paver.setuputils
import pkg_resources
#pylint: disable=unused-import
from runestone import build  # build is called implicitly by the paver driver.

paver.setuputils.install_distutils_tasks()

sys.path.append(os.getcwd())

home_dir = os.getcwd()
master_url = 'http://127.0.0.1:8000'
master_app = 'runestone'
serving_dir = "./_build"
dest = "../../static"
version = pkg_resources.require("runestone")[0].version

options(
    sphinx = Bunch(docroot=".",),

    build = Bunch(
        builddir="./_build",
        sourcedir="_intermediate",
        outdir="./_build",
        confdir=".",
        project_name = "Информатика и рачунарство за седми разред",

        # leave template_args empty, use html_context from conf.py
        template_args= {}
    )
)
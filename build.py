import shutil
from pathlib import Path

from staticjinja import Site
from yaml import Loader, load

import sass

def data():
    data_dict = {}
    yaml = Path("./data").glob("*.yaml")
    data_dict = {file_path.stem: load(file_path.open(), Loader=Loader) for file_path in yaml}

    return data_dict

buildpath = Path('output')

if buildpath.exists() and buildpath.is_dir():
    shutil.rmtree(buildpath)

if __name__ == "__main__":

    site = Site.make_site()
    site.outpath=buildpath
    site.contexts=[(".*.html", data)]
    # disable automatic reloading
    site.render(use_reloader=False)

    # copy the static folder
    shutil.copytree('static', buildpath / 'static')

    # compile sass to css
    sass.compile(dirname=('sass', buildpath / 'static/css'))

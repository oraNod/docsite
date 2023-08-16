import shutil
from pathlib import Path

from staticjinja import Site
from yaml import Loader, load

import sass


def data():
    yaml = Path("./data").glob("*.yaml")
    data_dict = {
        file_path.stem: load(file_path.read_text(), Loader=Loader) for file_path in yaml
    }

    return data_dict


def clean_buildpath(output_dir):
    shutil.rmtree(output_dir, ignore_errors=True)


def main():
    buildpath = Path("output")
    clean_buildpath(buildpath)

    site = Site.make_site()
    site.outpath = buildpath
    site.contexts = [(".*.html", data)]
    # disable automatic reloading
    site.render(use_reloader=False)

    # copy the static folder
    shutil.copytree("static", buildpath / "static")

    # compile sass to css
    sass.compile(dirname=("sass", buildpath / "static/css"))


if __name__ == "__main__":
    main()

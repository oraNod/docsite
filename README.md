# Ansible doc project resources

This repository holds several resources to enable contributors to work with Ansible documentation projects.

## Repository overview

```
.
├── docs                    # Project documentation.
│   ├── index.md            # Sample top-level page for MKDocs builds.
│   └── requirements.txt    # Packages for building MKDocs projects.
├── .readthedocs.yaml       # Sample configuration for Read The Docs hosting.
├── mkdocs.yml              # Sample configuration for MKDocs projects.
└── README.md               # This README file.
```

## Setting up MKDocs

If your project uses Markdown as the format for documentation pages, you can add MKDocs scaffolding to set up a docs build with the Ansible community theme.

### Before you begin

- [Install Python3](https://realpython.com/installing-python/).
- Clone this repository.
    ```
    git clone <git-repo>
    ```

### Build the MKDocs example

Complete the following steps to build some example HTML with MKDocs:

1. Create a Python virtual environment.
    ```
    python3 -m venv venv
    ```
2. Activate your virtual environment to start using it.
    ```
    source venv/bin/activate
    ```
3. Make sure your `pip` package manager is up to date.
    ```
    python3 -m pip install --upgrade pip
    ```
4. Install `mkdocs` and other required packages.
    ```
    python3 -m pip install -r docs/requirements.txt
    ```
5. Build some docs.
    ```
    mkdocs build
    ```

If the command runs successfully, you see the following messages:

```
INFO     -  Cleaning site directory
INFO     -  Building documentation to directory: /home/path/to/clone/site
INFO     -  Documentation built in 4.45 seconds
```

Open the generated HTML in your browser, as in the following example:

```
firefox site/index.html
```

Congrats!
Now you can setup your project to build docs with MKDocs.

### Install MKDocs in your project

The first thing to do is install the `mkdocs` package as part of your project.
You can do this in either of the following ways:

- Adding MKDocs to a Python `requirements.txt` file. This is a convenient way to install `mkdocs` along with other packages like the Ansible community theme for MKDocs, `mkdocs-ansible`.
- Adding the `pip install mkdocs` command to your project README or contributor file.

For convenience you can copy `docs/requirements.txt` from this repository to your project.

```
cp ./docs/requirements.txt path/to/project/docs/requirements.txt
```

### Add MKDocs configuration

After you install MKDocs in your project, you need to provide configuration in an `mkdocs.yaml` file.
You can do this in either of the following ways:

- Copy the MKDocs template in this repository.
- Initialize a new project with the `mkdocs new <project-name>` command. This command creates a `docs` folder and shell `mkdocs.yml` file in your project. An advantage of this approach is that you start with a "clean" project that has minimal requirements.

```
cp ./mkdocs.yaml path/to/project/mkdocs.yaml
```

### Adding documentation pages

At this point your project should have a directory structure such as:

```
.
├── docs                    # Documentation files in markdown
├── mkdocs.yml              # MKDocs configuration file
└── site                    # MKDocs build directory
```

Under the `docs` folder you should have a top-level `index.md` page like this:

```
.
├── docs
│   └── index.md
```

For example, to document configuration options you could add a `configuration.md` page like this:

```
.
├── docs
│   ├── configuration.md
│   └── index.md
```

Open `mkdocs.yml` and add the configuration page under the `nav:` key like this:

```
.
nav:
  - My Project Name Documentation:
      - home: index.md
      - configuration.md
```

Running the `mkdocs build` command should then generate `site/configuration.html`.

## Setting up Sphinx

You know what time it is.

## Adding projects to Read The Docs

Need to explain `.readthedocs.yaml`.

## Using tox and nox

General overview and comparison with Python venvs.

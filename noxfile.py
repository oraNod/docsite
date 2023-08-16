import os
from pathlib import Path

import nox
import subprocess

@nox.session
def build(session):
    session.install(
    "-r",
    "requirements.in",
    "-c",
    "requirements.txt",
    )
    session.run("python", "build.py")

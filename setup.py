import sys

from setuptools import setup
from setuptools_scm import get_version

# Place the directory containing _version_git on the path
sys.path.insert(0, "test")

# Use the version module to guess the next development version
version_string = get_version(
)

setup(
    version=version_string,
    setup_requires=["setuptools_scm"],
)
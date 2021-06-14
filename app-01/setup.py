from setuptools import setup

# see https://github.com/pypa/sampleproject/blob/main/setup.py
setup(
    name="app",
    version="0.0.1",
    packages=["app"],
    entry_points={"console_scripts": ["app = app.__main__:main"]},
)

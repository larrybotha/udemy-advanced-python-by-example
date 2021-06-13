from setuptools import setup

setup(
    name="app",
    version="0.0.1",
    packages=["app"],
    entry_points={"console_scripts": ["app = app.__main__:main"]},
)

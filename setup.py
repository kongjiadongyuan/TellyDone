from setuptools import setup, find_packages

required_packages = ["click", "trogon", "apprise"]

setup(
    name="TellyDone",
    version="0.0.1",
    install_requires=required_packages,
    packages=find_packages(),
    author="kongjiadongyuan",
    author_email="zhaggbl@outlook.com",
    description="A command-line utility that reminds you when your bash commands have finished.",
    license="MIT",
    entry_points={"console_scripts": ["telly=telly_done.main:cli"]},
)

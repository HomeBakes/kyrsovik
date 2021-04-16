from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="kyrsovik",
    version="0.0.1",
    author="Oleg kalygin",
    author_email="oleg.kalyugin2001@mail.ru",
    description="Just a student project",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/HomeBakes/kyrsovik",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.9.4",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
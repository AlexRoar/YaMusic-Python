#  Copyright (c) 2019.
#  Designed and codded with love by Aleksander Dremov
#
#
#
#

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyYaMusic",
    version="0.3.8",
    author="Alex Dremov",
    author_email="dremov.me@gmail.com",
    description="Yandex Music python environment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlexRoar/YaMusic-Python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
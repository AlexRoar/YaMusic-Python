#  Copyright (c) 2019.
#  Designed and codded with love by Aleksander Dremov
#
#
#
# koxsok-takboK-wujhi4

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyYaMusic",
    version="0.3.15",
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
    install_requires=[
        "bleach>=3.1.0",
        "certifi>=2019.3.9",
        "chardet>=3.0.4",
        "docutils>=0.14",
        "idna>=2.8",
        "Js2Py>=0.63",
        "pkginfo>=1.5.0.1",
        "playsound>=1.2.2",
        "Pygments>=2.3.1",
        "pyjsparser>=2.7.1",
        "pytz>=2019.1",
        "readme-renderer>=24.0",
        "requests>=2.21.0",
        "requests-toolbelt>=0.9.1",
        "six>=1.12.0",
        "tqdm>=4.31.1",
        "twine>=1.13.0",
        "tzlocal>=1.5.1",
        "urllib3>=1.24.2",
        "webencodings>=0.5.1"
    ]
)

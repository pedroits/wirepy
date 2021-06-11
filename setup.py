#!/usr/bin/env python

from setuptools import setup, find_packages

install_requires = []

setup(
    name="wirepy",
    version="0.0.3",
    author="Pedro Ivo",
    author_email="pedro.its@gmail.com",
    url="https://github.com/pedroits/wirepy",
    description="Python module to use Wirecard payment system",
    keywords=["wirecard", "payment", "payment gateway"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    license="GPL",
    packages=find_packages(),
    zip_safe=True,
    install_requires=install_requires,
    include_package_data=True
)
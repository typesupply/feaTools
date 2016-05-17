#!/usr/bin/env python

from setuptools import setup

setup(name = "feaTools",
      version = "0.1",
      description = "A library for interacting with .fea files.",
      author = "Tal Leming",
      author_email = "tal@typesupply.com",
      url = "https://github.com/typesupply/feaTools",
      license = "MIT",
      packages = [
              "feaTools",
              "feaTools.writers",
      ],
      package_dir = {"":"Lib"},
)

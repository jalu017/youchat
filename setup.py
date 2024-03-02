#!/usr/bin/env python

from setuptools import setup, find_packages
from wechat import VERSION

url="https://github.com/jalu017/youchat"

long_description="youchat Python SDK"

setup(name="youhat",
      version=VERSION,
      description=long_description,
      maintainer="jalu 017",
      maintainer_email="bebeknganjian@gmail.com",
      url = url,
      long_description=long_description,
      install_requires = ['requests'],
      packages=find_packages('.'),
     )



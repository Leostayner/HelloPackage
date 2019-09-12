from setuptools import setup

setup(name="my_hello_leonardo",
      version="0.1",
      packages=["my_hello"],
      install_requires=["pytest>=1.0"],
      scripts=["scripts/hello.py"])
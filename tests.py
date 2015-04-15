#! /usr/bin/env python
import unittest
from colour_runner.runner import ColourTextTestRunner
from os import path


def thisDir():
    return path.dirname(path.realpath(__file__))

loader = unittest.TestLoader()
tests = loader.discover('.', pattern="test_*.py")
runner = ColourTextTestRunner()
runner.run(tests)

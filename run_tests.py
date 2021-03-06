# -*- coding: utf-8 -*-
import unittest

from tests.functional.spiders import afpy

test_modules = [afpy, ]

suite = unittest.TestSuite()

for test_module in test_modules:
    suite.addTest(unittest.defaultTestLoader.loadTestsFromModule(test_module))

test_result = unittest.TextTestRunner().run(suite)

if test_result.failures or test_result.errors:
    exit(1)

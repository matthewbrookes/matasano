import unittest
import tests.setone

test_suite = unittest.TestSuite()
set1 = tests.setone.suite()
test_suite.addTest(set1)

runner = unittest.TextTestRunner()
runner.run(test_suite)

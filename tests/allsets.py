import unittest
import tests.setone
import tests.settwo

test_suite = unittest.TestSuite()
set1 = tests.setone.suite()
test_suite.addTest(set1)
set2 = tests.settwo.suite()
test_suite.addTest(set2)

runner = unittest.TextTestRunner()
runner.run(test_suite)

import unittest
import tests.test_setone
import tests.test_settwo

test_suite = unittest.TestSuite()
set1 = tests.test_setone.suite()
test_suite.addTest(set1)
set2 = tests.test_settwo.suite()
test_suite.addTest(set2)

runner = unittest.TextTestRunner()
runner.run(test_suite)

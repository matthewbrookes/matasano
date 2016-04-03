import unittest
from utils import *

class SetTwoTests(unittest.TestCase):
    """ Tests for Matasano Set Two """
    def test_ChallengeNine(self):
        plaintext = "YELLOW SUBMARINE"
        block_length = 20
        expected_result = "YELLOW SUBMARINE\x04\x04\x04\x04"
        self.assertEqual(expected_result,
                         ChallengeUtils.PKCS7padding(plaintext, block_length))


def suite():
    suite = unittest.TestSuite()
    suite.addTest(SetTwoTests("test_ChallengeNine"))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

import unittest
from utils import *
from settwo import *

class SetTwoTests(unittest.TestCase):
    """ Tests for Matasano Set Two """
    def test_ChallengeNine(self):
        plaintext = "YELLOW SUBMARINE"
        block_length = 20
        expected_result = "YELLOW SUBMARINE\x04\x04\x04\x04"
        self.assertEqual(expected_result,
                         ChallengeUtils.PKCS7padding(plaintext, block_length))
    def test_ChallengeTen(self):
        expected_result_file = open("./challenge-data/10-decrypted.txt")
        expected_result = expected_result_file.read()
        expected_result_file.close()
        self.assertEqual(expected_result, challenge10.main())


def suite():
    suite = unittest.TestSuite()
    suite.addTest(SetTwoTests("test_ChallengeNine"))
    suite.addTest(SetTwoTests("test_ChallengeTen"))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

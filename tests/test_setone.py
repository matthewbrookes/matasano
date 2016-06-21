import unittest
from setone import *
from utils import *
from base64 import b16encode

class SetOneTests(unittest.TestCase):
    """ Tests for Matasano Set One """
    def test_ChallengeOne(self):
        hex_string = ("49276d206b696c6c696e6720796f757220627261696e206c696b"
                        "65206120706f69736f6e6f7573206d757368726f6f6d")
        base64 = ("SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11"
                    "c2hyb29t")
        self.assertEqual(base64.encode(), Conversion.hex2base64(hex_string))

    def test_ChallengeTwo(self):
        hex_string1 = "1c0111001f010100061a024b53535009181c"
        hex_string2 = "686974207468652062756c6c277320657965"
        result = "746865206b696420646f6e277420706c6179"
        xor = Bitwise.fixedXOR(hex_string1, hex_string2)
        self.assertEqual(result, xor)

    def test_ChallengeThree(self):
        encrypted = ("1b37373331363f78151b7f2b783431333d78397828372d363c783"
                     "73e783a393b3736")
        decrypted = "Cooking MC's like a pound of bacon"
        self.assertEqual(decrypted,
                         ChallengeUtils.guess_single_character_xor(encrypted))

    def test_ChallengeFour(self):
        expected_result = "Now that the party is jumping\n"
        self.assertEqual(expected_result, challenge4.main())

    def test_ChallengeFive(self):
        plaintext = ("Burning 'em, if you ain't quick and nimble\n"
                     "I go crazy when I hear a cymbal").encode()
        key = "ICE"
        expected_result = ("0b3637272a2b2e63622c2e69692a23693a2a3c6324202d62"
                           "3d63343c2a26226324272765272a282b2f20430a652e2c65"
                           "2a3124333a653e2b2027630c692b20283165286326302e27"
                           "282f")
        self.assertEqual(expected_result,
                         Bitwise.repeat_key_XOR(b16encode(plaintext), key))

    def test_ChallengeSix(self):
        expected_result_file = open("./challenge-data/6-decrypted.txt")
        expected_result = expected_result_file.read()
        expected_result_file.close()
        self.assertEqual(expected_result, challenge6.main())

    def test_ChallengeSeven(self):
        expected_result_file = open("./challenge-data/7-decrypted.txt")
        expected_result = expected_result_file.read()
        expected_result_file.close()
        self.assertEqual(expected_result, challenge7.main())

    def test_ChallengeEight(self):
        expected_result = ("d880619740a8a19b7840a8a31c810a3d08649af70dc06f4"
                           "fd5d2d69c744cd283e2dd052f6b641dbf9d11b0348542bb"
                           "5708649af70dc06f4fd5d2d69c744cd2839475c9dfdbc1d"
                           "46597949d9c7e82bf5a08649af70dc06f4fd5d2d69c744c"
                           "d28397a93eab8d6aecd566489154789a6b0308649af70dc"
                           "06f4fd5d2d69c744cd283d403180c98c8f6db1f2a3f9c40"
                           "40deb0ab51b29933f2c123c58386b06fba186a")
        self.assertEqual(expected_result, challenge8.main())

def suite():
    suite = unittest.TestSuite()
    suite.addTest(SetOneTests("test_ChallengeOne"))
    suite.addTest(SetOneTests("test_ChallengeTwo"))
    suite.addTest(SetOneTests("test_ChallengeThree"))
    suite.addTest(SetOneTests("test_ChallengeFour"))
    suite.addTest(SetOneTests("test_ChallengeFive"))
    suite.addTest(SetOneTests("test_ChallengeSix"))
    suite.addTest(SetOneTests("test_ChallengeSeven"))
    suite.addTest(SetOneTests("test_ChallengeEight"))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

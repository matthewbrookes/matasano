import unittest
import ChallengeUtils
import Conversion
import Bitwise
import challenge4
import challenge6
import challenge7
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

if __name__ == '__main__':
    unittest.main()

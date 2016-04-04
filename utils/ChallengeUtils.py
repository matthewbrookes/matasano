from . import EnglishUtils
import string
from . import Bitwise
import binascii
from Crypto.Cipher import AES
import pdb
import base64

def guess_single_character_xor(hex_string):
    ''' Returns the best guess of xoring hex_string with a character '''
    best_guess = hex_string
    best_score = EnglishUtils.score_word(hex_string)
    for i in range(256):
        characters = single_character_xor(hex_string, i)
        score = EnglishUtils.score_word(characters)
        if score > best_score:
            best_score = score
            best_guess = characters
    return best_guess

def single_character_xor(hex_string, ordinal):
    digit_as_hex_string = "{0:0{1}x}".format(ordinal, 2)
    # Split hex string into individual bytes
    bytes_in_hex = [
        hex_string[i: i+2] for i in range(0, len(hex_string), 2)
    ]
    characters = ''
    for byte in bytes_in_hex:
        char = Bitwise.fixedXOR(byte, digit_as_hex_string)
        characters += chr(int(char, 16))
    return characters

def single_character_most_english_xor(hex_string):
    best_score = 0
    best_guess = 0
    for i in range(256):
        # XOR each byte and add to score if result is ascii
        score = 0
        for j in range(0, len(hex_string), 2):
            char = single_character_xor(hex_string[2*j: 2*(j+1)], i)
            if char in string.ascii_letters or char in {':', ';', ' '}:
                score += 1
        if score > best_score:
            best_score = score
            best_guess = i
    return best_guess

def decrypt_aes_ecb(ciphertext, key):
    decryption_suite = AES.new(key)
    return decryption_suite.decrypt(ciphertext)

def encrypt_aes_ecb(plaintext, key):
    encryption_suite = AES.new(key)
    return encryption_suite.encrypt(plaintext)

def decrypt_aes_cbc(ciphertext, key, iv):
    ''' Decrypt a ciphertext in AES CBC form '''
    # Pre: key same size as initialisation vector
    # Pre: argument in byte hex form (e.g. "\x23\x10A$")
    # Pre: all arguments length multiples of 16
    # Post: returns in byte hex form
    c = []
    c.append(iv)
    blocksize = len(key)
    for i in range(0, len(ciphertext), blocksize):
        c.append(ciphertext[i: i+blocksize])
    p = []
    for i in range(int(len(ciphertext)/blocksize)):
        last_cipher_block = c[i]
        decoded = decrypt_aes_ecb(c[i+1], key)
        xorstring = b''
        for (x, y) in zip (decoded, last_cipher_block):
            xor = x^y
            xorstring += xor.to_bytes(1, "big")
        p.append(xorstring)
    return (b'').join(p)


def encrypt_aes_cbc(plaintext, key, iv):
    ''' Encrypt plaintext in AES CBC form '''
    # Pre: key same size as initialisation vector
    # Pre: argument in byte hex form (e.g. "\x23\x10A$")
    # Pre: all arguments length multiples of 16
    # Post: returns in byte hex form
    c = []
    c.append(iv)
    blocksize = len(key)
    for i in range(int(len(plaintext)/blocksize)):
        plaintext_block = plaintext[i*blocksize: (i+1)*blocksize]
        last_cipher_block = c[i]
        xorstring = b''
        for (x, y) in zip (plaintext_block, last_cipher_block):
            xor = x^y
            xorstring += xor.to_bytes(1, "big")
        encrypted = encrypt_aes_ecb(xorstring, key)
        c.append(encrypted)
    return (b'').join(c[1:])


def hamming_distance(string1, string2):
    ''' Returns hamming distance between two equal length strings '''
    string1_encoded = string1.encode()
    string2_encoded = string2.encode()
    distance = 0
    for (x, y) in zip (string1_encoded, string2_encoded):
        xor = x^y
        while xor > 0:
            distance += xor & 1
            xor >>= 1
    return distance

def hamming_distance_hex(hex1, hex2):
    ''' Returns hamming distance between two hex bytes as strings'''
    xor = int(hex1, 16) ^ int(hex2, 16)
    distance = 0
    while xor > 0:
        distance += xor & 1
        xor >>= 1
    return distance

def PKCS7padding(string, num_bytes):
    num_bytes_to_append = num_bytes - len(string)
    padded_string = string
    for i in range(num_bytes_to_append):
        padded_string += chr(num_bytes_to_append)
    return padded_string

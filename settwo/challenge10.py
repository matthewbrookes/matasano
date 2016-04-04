import base64
import pdb
from utils import ChallengeUtils
import binascii

def main():
    encrypted_file = open("./challenge-data/10.txt")
    encrypted_base64 = encrypted_file.read()
    encrypted_file.close()
    ciphertext = (base64.b64decode(encrypted_base64))
    key = b"YELLOW SUBMARINE"
    iv = b""
    for i in range(16):
        iv += b'\x00'
    plaintext = ChallengeUtils.decrypt_aes_cbc(ciphertext, key, iv)
    return plaintext.decode()

if __name__ == "__main__":
    print(main())

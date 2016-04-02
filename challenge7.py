import base64
from Crypto.Cipher import AES

def main():
    encrypted_file = open("./challenge-data/7.txt")
    encrypted_base64 = encrypted_file.read().rstrip()
    encrypted_file.close()
    decryption_suite = AES.new(b"YELLOW SUBMARINE")
    encrypted_string = base64.b64decode(encrypted_base64)
    return decryption_suite.decrypt(encrypted_string).decode()

if __name__ == "__main__":
    print(main())

import base64
from utils import ChallengeUtils

def main():
    encrypted_file = open("./challenge-data/7.txt")
    encrypted_base64 = encrypted_file.read().rstrip()
    encrypted_file.close()
    encrypted_string = base64.b64decode(encrypted_base64)
    decrypted = ChallengeUtils.decrypt_aes_ecb(
                                               encrypted_string,
                                               b"YELLOW SUBMARINE")
    return decrypted.decode()

if __name__ == "__main__":
    print(main())

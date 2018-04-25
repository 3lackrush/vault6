__author__ = 'Kios'
__description__ = "Vault6 is made to protect your data"
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes


class Vault6Encrypt(object):

    def __init__(self, filename, location):
        self.filename = filename
        self.location = location

    def _encrypt(self):
        with open(self.filename, 'rb') as f:
            data = f.read()

        with open(self._save_location(), 'wb') as encrypted_file:
            recipient_key = RSA.import_key(open('./pem/vault6_public_rsa.pem').read())
            session_key = get_random_bytes(16)
            cipher_rsa =  PKCS1_OAEP.new(recipient_key)
            encrypted_file.write(cipher_rsa.encrypt(session_key))
            cipher_aes = AES.new(session_key, AES.MODE_EAX)
            ciphertext, tag = cipher_aes.encrypt_and_digest(data)
            encrypted_file.write(cipher_aes.nonce)
            encrypted_file.write(tag)
            encrypted_file.write(ciphertext)

        f.close()
        encrypted_file.close()

    def _encrypt_filename(self):
        return self.filename + ".vault6"

    def _save_location(self):
        filename = self._encrypt_filename()
        path = self.location + "/" + filename
        return path

    def run(self):
        self._encrypt()
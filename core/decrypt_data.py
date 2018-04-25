__author__ = 'Kios'
__description__ = "Vault6 is made to protect your data"

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

class Vault6Decrypt(object):
    def __init__(self, filename, password, location):
        self.filename = filename
        self.password = password
        self.location = location

    def _decrypt(self):
        code = self.password
        with open(self._origin_path(), 'rb') as encrypted_file:
            private_key = RSA.import_key(open("./pem/vault6_private_rsa_key.bin").read(), passphrase=code)
            enc_session_key, nonce, tag, ciphertext = [encrypted_file.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)]
            cipher_rsa = PKCS1_OAEP.new(private_key)
            session_key = cipher_rsa.decrypt(enc_session_key)
            cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
            data = cipher_aes.decrypt_and_verify(ciphertext, tag)

        with open(self._save_location(), 'wb') as decrypt_file:
            decrypt_file.write(data)

        encrypted_file.close()
        decrypt_file.close()

    def _decrypt_filename(self):
        filename = self.filename.split(".vault6")[0]
        return filename

    def _origin_path(self):
        path = self.location + "/" + self.filename
        return path

    def _save_location(self):
        path = self.location + "/" + self._decrypt_filename()
        return path

    def run(self):
        self._decrypt()

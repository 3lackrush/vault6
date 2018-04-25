__author__ = 'Kios'
__description__ = "Vault6 is made to protect your data"

from Crypto.PublicKey import RSA

class genRSA:

    def __init__(self, passwd):
        self.passwd = passwd

    def _generateKey(self):
        key = RSA.generate(2048)
        encrypted_key = key.exportKey(passphrase=self.passwd, pkcs=8, protection="scryptAndAES128-CBC")
        with open('./pem/vault6_private_rsa_key.bin', 'wb') as f:
            f.write(encrypted_key)
        with open('./pem/vault6_public_rsa.pem', 'wb') as f:
            f.write(key.publickey().exportKey())

        f.close()

    def run(self):
        self._generateKey()
        print("Public key and Pem generate complete!")
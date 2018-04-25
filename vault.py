__author__ = 'Kios'
__description__ = "Vault6 is made to protect your data"

import getpass
import argparse
import sys,time
from utils.banner import Banner, Note
from termcolor import colored
from core.encrypt_data import Vault6Encrypt
from core.decrypt_data import Vault6Decrypt
from core.gen_rsa import genRSA

def Usage():
    print(colored(Banner, "green"))
    print(colored(Note, "red"))

def EncryptFile(filename, location):
	obj1 = Vault6Encrypt(filename, location)
	obj1.run()
	print("Encrypt file successful!")

def DecryptFile(filename, location, code):
	obj1 = Vault6Decrypt(filename, code, location)
	obj1.run()
	print("Decrypt file successful!")
		
def GenRSAKEY(code):
	passwd = code
	obj1 = genRSA(passwd)
	obj1.run()
	print("Process complete!")

if __name__ == '__main__':
	Usage()
	parser = argparse.ArgumentParser(description='Vault6 is made to protect your data, pls generate your own key please!')
	parser.add_argument('-g', '--generate', metavar="generate",required=False, action="store", dest="generate",help='Generate RSA key')
	parser.add_argument('-f', '--file', metavar="filename", required=False, action="store", dest="filename", help="Input filename")
	parser.add_argument('-p', '--path', metavar="path", required=False, action="store", dest="path", help="Input path to store the encrypted file")
	parser.add_argument('-m', '--method', metavar="method", required=False, action="store", choices={'encrypt','decrypt'}, default='encrypt', dest="method", help="choose method to operate!")
	args = parser.parse_args()
	if args.generate == 'cert':
		code = getpass.getpass()
		GenRSAKEY(code)
		print(colored("[+] Generate key with code successful!","green"))
	

	if args.method == 'encrypt':
		if args.filename != None and args.path != None:
			EncryptFile(args.filename, args.path)
		else:
			print(colored("[*] something went wrong! please correct your command first!", "red"))
	elif args.method == 'decrypt':
		if args.filename != None and args.path != None:
			code = getpass.getpass()
			DecryptFile(args.filename, args.path, code)
		else:
			print(colored("[*] something went wrong! please correct your command first!", "red"))
	else:
		print(colored("[*] invalid command!"))


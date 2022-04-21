import random
from alphabet import *

def vernam_cipher(input_file):
	with open(input_file, 'rb') as inf:
		keyf = open('Vernam_key.txt', 'wb')
		outf = open('Vernam_encryption.txt', 'wb')
		byte_in = inf.read(1)
		while byte_in:
			new_key = random.randint(0, 255)
			new_byte = bytes([ord(byte_in) ^ new_key])
			outf.write(new_byte)
			keyf.write(bytes([new_key]))
			byte_in = inf.read(1)

def vernam_decipher(input_file):
	with open(input_file, 'rb') as inf:
		key = input('Enter the key file (path)): ')
		keyf = open(key, 'rb')
		outf = open('Vernam_decoding.txt', 'wb')
		byte_in = inf.read(1)
		while byte_in:
			new_key = keyf.read(1)
			new_byte = bytes([ord(new_key) ^ ord(byte_in)])
			outf.write(new_byte)
			byte_in = inf.read(1)

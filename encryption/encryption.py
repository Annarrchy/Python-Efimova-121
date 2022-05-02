#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import random
import click
import caesar_ciph
import vigenere_ciph
import vernam_ciph
import caesar_an
	
def encrypt(cipher, input_file, lang, key):
	if cipher == 'Caesar_cipher' or cipher == 'cac':
		result = caesar_ciph.caesar_cipher(input_file, lang, key)
	if cipher == 'Caesar_decipher' or cipher == 'cad':
		result = caesar_ciph.caesar_decipher(input_file, lang, key)
	if cipher == 'Vigenere_cipher' or cipher == 'vic':
		result = vigenere_ciph.vigenere_cipher(input_file, lang, key)
	if cipher == 'Vigenere_decipher' or cipher == 'vid':
		result = vigenere_ciph.vigenere_decipher(input_file, lang, key)
	if cipher == 'Vernam_cipher' or cipher == 'vec':
		result = vernam_ciph.vernam_cipher(input_file)
		with open('Vernam_encryption.txt', 'r', encoding = 'Latin-1') as file:
		    result = 'Cipher: ' + file.read()
		'''with open(input_file, 'r', encoding = 'utf-8') as file:
		    print('Input_text: ', file.read())'''
	if cipher == 'Vernam_decipher' or cipher == 'ved':
		vernam_ciph.vernam_decipher(input_file, key)
		with open('Vernam_decoding.txt', 'r', encoding = 'utf-8') as file:
		    result = 'Decipher: ' + file.read()
		'''with open(input_file, 'r', encoding = 'Latin-1') as file:
		    print('Input_text: ', file.read())'''
	if cipher == 'Caesar_analysis' or cipher == 'can':
		result = caesar_an.caesar_analysis(input_file, lang)
	return result

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import random
import click
import caesar_ciph
import vigenere_ciph
import vernam_ciph
import caesar_an
	
@click.command()
@click.option("--cipher", "-c", type=str, 
              help="Use one of: Caesar_cipher (cac), Caesar_decipher (cad), Vigenere_cipher (vic), Vigenere_decipher (vid), Vernam_cipher (vec), Vernam_decipher (ved), Caesar_analysis (can)")
@click.option("--input_file", "-i", type=click.Path(exists=True, file_okay=True), required=True,
              help="Source of input file")
def main(cipher, input_file):
	if cipher == 'Caesar_cipher' or cipher == 'cac':
		caesar_ciph.caesar_cipher(input_file)
	if cipher == 'Caesar_decipher' or cipher == 'cad':
		caesar_ciph.caesar_decipher(input_file)
	if cipher == 'Vigenere_cipher' or cipher == 'vic':
		vigenere_ciph.vigenere_cipher(input_file)
	if cipher == 'Vigenere_decipher' or cipher == 'vid':
		vigenere_ciph.vigenere_decipher(input_file)
	if cipher == 'Vernam_cipher' or cipher == 'vec':
		vernam_ciph.vernam_cipher(input_file)
		with open('Vernam_encryption.txt', 'r', encoding = 'Latin-1') as file:
		    print('Cipher: ', file.read())
		with open(input_file, 'r', encoding = 'utf-8') as file:
		    print('Input_text: ', file.read())
	if cipher == 'Vernam_decipher' or cipher == 'ved':
		vernam_ciph.vernam_decipher(input_file)
		with open('Vernam_decoding.txt', 'r', encoding = 'utf-8') as file:
		    print('Decipher: ', file.read())
		with open(input_file, 'r', encoding = 'Latin-1') as file:
		    print('Input_text: ', file.read())
	if cipher == 'Caesar_analysis' or cipher == 'can':
		caesar_an.caesar_analysis(input_file)
	
if __name__ == "__main__":
	main()


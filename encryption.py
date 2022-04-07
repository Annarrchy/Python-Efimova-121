#!/usr/bin/env python3
import os
import random
import click

#alphabets
alphabet =  'ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet_vig =  'ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ ><?.,/\|@#$!^&*()_+=-1234567890`~;:"[]{}'
alphabet_vigru =  'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ ><?.,/\|@#$!^&*()_+=-1234567890`~;:"[]{}'
alphabet_vigeu =  'ABCDEFGHIJKLMNOPQRSTUVWXYZ ><?.,/\|@#$!^&*()_+=-1234567890`~;:"[]{}'
alphabet_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

def Caesar_cipher(input_file):
	lang = input('Choose language: RU/EU/BOTH: ')
	with open(input_file, 'r', encoding = 'utf-8') as f:
	    text = f.read().upper()
	#key of encryption
	shift = int(input('Enter the shift value (number)): ')) 
	keyf = open('Caesar_key.txt', 'w')
	keyf.write(str(shift))
	result = ''
	alpha = ''
	if lang == "BOTH":
		alpha=alphabet
	if lang == "RU":
		alpha=alphabet_RU
	if lang == "EU":
		alpha=alphabet_EU
	
	for i in text:
		place = alpha.find(i)
		new_place = (place + shift) % len(alpha)
		if i in alphabet:
			result += alpha[new_place]
		else:
			result += i
			
	print('Cipher:', result)
	print('Input text: ', text)
	res = open('Caesar_encryption.txt', 'w')
	res.write(result)

def Caesar_decipher(input_file):
	lang = input('Choose language: RU/EU/BOTH: ')
	with open(input_file, 'r') as f:
	    text = f.read().upper()
	
	shift = int(input('Enter the shift value (number)): ')) 
	result = ''
	alpha = ''
	if lang == "BOTH":
		alpha=alphabet
	if lang == "RU":
		alpha=alphabet_RU
	if lang == "EU":
		alpha=alphabet_EU
	
	for i in text:
		place = alpha.find(i)
		new_place = (place - shift) % len(alpha)
		if i in alphabet:
			result += alpha[new_place]
		else:
			result += i
			
	print('Decipher:', result)
	print('Input text: ', text)
	res = open('Caesar_decoding.txt', 'w')
	res.write(result)

def form_dict(lang):
	d = {}
	iter = 0
	
	alphab = ''
	if lang == "BOTH":
		alphab = alphabet_vig
	if lang == "RU":
		alphab = alphabet_vigru
	if lang == "EU":
		alphab = alphabet_vigeu
		
	for i in alphab:
	    d[iter] = i
	    iter = iter + 1
	return d

def encode_val(word, lang):
    list_code = []
    lent = len(word)
    d = form_dict(lang)

    for w in range(lent):
        for value in d:
            if word[w] == d[value]:
               list_code.append(value) 
    return list_code

def comparator(value, key):
    len_key = len(key)
    dic = {}
    iter = 0
    full = 0

    for i in value:
        dic[full] = [i,key[iter]]
        full = full + 1
        iter = iter +1
        if (iter >= len_key):
            iter = 0 
    return dic 

def full_encode(value, key, lang):
    dic = comparator(value, key)
    lis = []
    d = form_dict(lang)
    
    for v in dic:
        go = (dic[v][0]+dic[v][1]) % len(d)
        lis.append(go) 
    return lis

def decode_val(list_in, lang):
	list_code = []
	lent = len(list_in)
	d = form_dict(lang)
	count=0
	for i in range(lent):
		for value in d:
			if list_in[i] == value:
				list_code.append(d[value])
	return list_code

def full_decode(value, key, lang):
    dic = comparator(value, key)
    d = form_dict(lang) 
    lis =[]

    for v in dic:
        go = (dic[v][0]-dic[v][1]+len(d)) % len(d)
        lis.append(go) 
    return lis

def Vigenere_cipher(input_file):
	lang = input('Choose language: RU/EU/BOTH: ')
	with open(input_file, 'r', encoding = 'utf-8') as f:
	    text = f.read().upper()
	key = input('Enter the key value (word): ')
	keyf = open('Vigenere_key.txt', 'w')
	keyf.write(key)
	key_encoded = encode_val(key.upper(), lang)
	value_encoded = encode_val(text, lang)
	shifre = full_encode(value_encoded, key_encoded, lang)
	result = decode_val(shifre, lang)
	decoded = full_decode(shifre, key_encoded, lang)
	
	res = open('Vigenere_encryption.txt', 'w')
	res.write(''.join(result))
	
	#in case you wanted to explore the process:
	#print ('Value: ', value_encoded)
	#print ('Key: ', key_encoded)
	#print ('Decode list:', decoded)
	print ('Cipher: ', ''.join(result))
	print ('Input text: ', text)
	
def Vigenere_decipher(input_file):
	lang = input('Choose language: RU/EU/BOTH: ')
	with open(input_file, 'r') as f:
	    text = f.read()
	key = input('Enter the key value (word): ')
	key_encoded = encode_val(key.upper(), lang)
	shifre = encode_val(text, lang)
	decoded = full_decode(shifre, key_encoded, lang)
	result = ''.join(decode_val(decoded, lang))
	res = open('Vigenere_decoding.txt', 'w')
	res.write(''.join(result))
	print ('Dechipher: ', result)
	print ('Input text: ', text)
	
def Vernam_cipher(input_file):
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

def Vernam_decipher(input_file):
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

def Caesar_analysis(input_file):
	lang = input('Choose language: RU/EU/BOTH: ')
	with open(input_file, 'r') as f:
	    text = f.read().upper()
	    
	if lang == "BOTH":
		alpha=alphabet
	if lang == "RU":
		alpha=alphabet_RU
	if lang == "EU":
		alpha=alphabet_EU
	ma = 0
	index = 0
	text_ind = 0
	for i in range(len(alpha)):
		count = 0
		for p in range(len(text)):
			if alpha[i] == text[p]:
				count += 1
		if ma < count:
			ma = count
			index = i + 1
			text_ind = p
	if lang == "RU":
		shift = abs(16 - index)
	elif lang == "EU":
		shift = abs(5 - index)
	else:
		count = 0
		for i in range(len(alphabet_EU)):
			if text[p] == alphabet_EU[i]:
				count = 1
				shift = abs(5 - index)
		if count == 0:
			shift = abs(42 - index)
	result = ''
	for i in text:
		place = alpha.find(i)
		new_place = (place - shift) % len(alpha)
		if i in alphabet:
			result += alpha[new_place]
		else:
			result += i
			
	print('Decipher:', result)
	print('Input text: ', text)
	res = open('Caesar_decoding.txt', 'w')
	res.write(result)
	
@click.command()
@click.option("--cipher", type=str, 
              help="Use one of: Caesar_cipher, Caesar_decipher, Vigenere_cipher, Vigenere_decipher, Vernam_cipher, Vernam_decipher, Caesar_analysis")
@click.option("--input_file", type=click.Path(exists=True, file_okay=True), required=True,
              help="Source of input file")
def main(cipher, input_file):
	if cipher == 'Caesar_cipher':
		Caesar_cipher(input_file)
	if cipher == 'Caesar_decipher':
		Caesar_decipher(input_file)
	if cipher == 'Vigenere_cipher':
		Vigenere_cipher(input_file)
	if cipher == 'Vigenere_decipher':
		Vigenere_decipher(input_file)
	if cipher == 'Vernam_cipher':
		Vernam_cipher(input_file)
		with open('Vernam_encryption.txt', 'r') as file:
		    print('Cipher: ', file.read())
		with open(input_file, 'r', encoding = 'utf-8') as file:
		    print('Input_text: ', file.read())
	if cipher == 'Vernam_decipher':
		Vernam_decipher(input_file)
		with open('Vernam_decoding.txt', 'r', encoding = 'utf-8') as file:
		    print('Decipher: ', file.read())
		with open(input_file, 'r') as file:
		    print('Input_text: ', file.read())
	if cipher == 'Caesar_analysis':
		Caesar_analysis(input_file)
	
if __name__ == "__main__":
	main()


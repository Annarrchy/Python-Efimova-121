from alphabet import *

def caesar_cipher(input_file, lang, key):
	with open(input_file, 'r', encoding = 'utf-8') as f:
	    text = f.read().upper()
	#key of encryption
	shift = int(key)
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
			
	#print('Cipher:', result)
	#print('Input text: ', text)
	res = open('Caesar_encryption.txt', 'w')
	res.write(result)
	return 'Cipher:', result

def caesar_decipher(input_file, lang, key):
	with open(input_file, 'r') as f:
	    text = f.read().upper()
	result = ''
	alpha = ''
	if lang == "BOTH":
		alpha=alphabet
	if lang == "RU":
		alpha=alphabet_RU
	if lang == "EU":
		alpha=alphabet_EU
	shift = int(key)
	
	for i in text:
		place = alpha.find(i)
		new_place = (place - shift) % len(alpha)
		if i in alphabet:
			result += alpha[new_place]
		else:
			result += i
			
	#print('Decipher:', result)
	#print('Input text: ', text)
	res = open('Caesar_decoding.txt', 'w')
	res.write(result)
	return 'Decipher:', result


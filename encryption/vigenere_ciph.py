from alphabet import *

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

def vigenere_cipher(input_file, lang, key):
	with open(input_file, 'r', encoding = 'utf-8') as f:
	    text = f.read().upper()
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
	#print ('Cipher: ', ''.join(result))
	#print ('Input text: ', text)
	return 'Cipher:', ''.join(result)
	
def vigenere_decipher(input_file, lang, key):
	with open(input_file, 'r') as f:
	    text = f.read()
	key_encoded = encode_val(key.upper(), lang)
	shifre = encode_val(text, lang)
	decoded = full_decode(shifre, key_encoded, lang)
	result = ''.join(decode_val(decoded, lang))
	res = open('Vigenere_decoding.txt', 'w')
	res.write(''.join(result))
	#print ('Dechipher: ', result)
	#print ('Input text: ', text)
	return 'Decipher:', ''.join(result)

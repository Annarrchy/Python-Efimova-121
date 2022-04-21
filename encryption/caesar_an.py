from alphabet import *

rate_BOTH = [0.082, 0.015, 0.028, 0.043, 0.13, 0.022, 0.02, 0.061, 0.07, 0.0015, 0.0077, 0.04, 0.024, 0.067, 0.075, 0.019, 0.00095, 0.06, 0.063, 0.091, 0.028, 0.0098, 0.024, 0.0015, 0.02, 0.00074, 0.062, 0.014, 0.038, 0.013, 0.025, 0.072, 0.00031, 0.007, 0.016, 0.062, 0.010, 0.028, 0.035, 0.026, 0.053, 0.09, 0.023, 0.04, 0.045, 0.053, 0.021, 0.002, 0.009, 0.004, 0.012, 0.006, 0.000312, 0.016, 0.014, 0.003, 0.006, 0.018]
rate_RU = [0.062, 0.014, 0.038, 0.013, 0.025, 0.072, 0.00031, 0.007, 0.016, 0.062, 0.010, 0.028, 0.035, 0.026, 0.053, 0.09, 0.023, 0.04, 0.045, 0.053, 0.021, 0.002, 0.009, 0.004, 0.012, 0.006, 0.003, 0.000312, 0.016, 0.014, 0.003, 0.006, 0.018]
rate_EN = [0.082, 0.015, 0.028, 0.043, 0.13, 0.022, 0.02, 0.061, 0.07, 0.0015, 0.0077, 0.04, 0.024, 0.067, 0.075, 0.019, 0.00095, 0.06, 0.063, 0.091, 0.028, 0.0098, 0.024, 0.0015, 0.02, 0.00074]

def find_shift(text, ord_alpha, rate_al, alpha):
	rate=[0 for _ in range(len(ord_alpha))]
	space = 0
	enru = False
	if len(ord_alpha) > len(alphabet_RU):
		enru = True
	for i in text:
		if i == ' ':
			space += 1
		elif i in alpha:
			rate[ord_alpha[i]] += 1
	rate = list(map(lambda x: x / (len(text) - space), rate))
	shifts = {i : 0 for i in range(len(ord_alpha))}
	for i in range(len(ord_alpha)):
		diff = 1
		sdv = 0
		for p in range(len(ord_alpha)):
			if diff > abs(rate[i] - rate_al[p]):
				if (enru == False) or (enru and ((i < 26 and p < 26) or (i > 25 and p > 25))):
					diff = abs(rate[i] - rate_al[p])
					sdv = p
		if i > sdv:
			sdv = i - sdv
		elif i < sdv:
			sdv = len(alpha) - sdv + i
		shifts[sdv] += 1
	
	shift = sorted(list(shifts.keys()), key=lambda x: shifts[x])[-1]
	return shift
		
		
	

def caesar_analysis(input_file):
	lang = input('Choose language: RU/EU/BOTH: ')
	with open(input_file, 'r') as f:
	    text = f.read().upper()
	
	if lang == "BOTH":
		alpha = alphabet
		rate_al = rate_BOTH
	if lang == "RU":
		alpha=alphabet_RU
		rate_al = rate_RU
	if lang == "EU":
		alpha=alphabet_EU
		rate_al = rate_EU
	ord_alpha = {}
	for i in range(len(alpha)):
		ord_alpha[alpha[i]] = i
	
	shift = find_shift(text, ord_alpha, rate_al, alpha)
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

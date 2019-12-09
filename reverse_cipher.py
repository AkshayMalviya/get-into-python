message = 'Three can keep secret, if two of them are dead.'
translated = ''

i = len(message) - 1
while i>=0:
	translated = translated + message[i]
	print(i, message[i], translated)
	i-=1
print(translated)
from urllib.request import urlopen
with urlopen('https://www.google.co.in/') as response:
	for line in response:
		line=line.decode('utf-8')
		#if 'EST' in line or 'EDT' in line:
		print(line)

def main():
	wfiles = ['negativeWords.txt', 'positiveWords.txt']

	for f in wfiles:
		text = open(f, 'r').read()
		wordict = dict()
		print "cleaning... %s"%f
		for x in text.split():
			x = x.strip().lower()
			if not x in wordict and x != '':
				wordict[x] = ''

		temp = sorted(wordict.keys())
		with open('new'+f, 'w') as f1:
			for w in temp:
				f1.write(w+'\n')
		f1.close()
		print "Done!"

if __name__ == '__main__':
	main()
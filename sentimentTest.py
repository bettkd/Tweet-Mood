
positiveWords = []
negativeWords = []

def loadWords(file1, file2):
	positiveWords.extend(open(file1, 'r').read().split())
	negativeWords.extend(open(file2, 'r').read().split())
	print '\n+ve and -ve words loaded..'

def main():

	loadWords(file1='newpositiveWords.txt', file2='newnegativeWords.txt')

	positiveFiles = ['recommendation1', 'recommendation2', 'recommendation3', 'recommendation4', 'recommendation5']
	negativeFiles = ['review1', 'review2', 'review3', 'review4', 'review5'] # bad hotel reviews



	print "\n## Positive Recommendations ##"
	print "============================"
	# positive files
	for f in positiveFiles:
		posF = [None]
		posF.extend(open(f, 'r').read().lower().split())
		p = determineAccuracy(posF, positiveWords, 1)
		n = determineAccuracy(posF, negativeWords, -1)
		h = p + n
		printStatus(h, f)



	print "\n##### Negative Reviews ######"
	print "============================"

	# negative files
	for f in negativeFiles:
		negF = [None]
		negF.extend(open(f, 'r').read().lower().split())
		p = determineAccuracy(negF, positiveWords, 1)
		h = determineAccuracy(negF, negativeWords, -1)
		printStatus(h, f)


def determineAccuracy(fileF, words, heuristic=1):
	sentCounter = 0

	sentiments = []
	for w in words:
		if w in fileF:
			sentiments.append(w)
			sentCounter += heuristic
	#print sentiments
	return sentCounter

def printStatus(h, f):
	if h > 0 :
		print "positive tone/emotion for %s. Count = %s"%(f, h)
	elif h == 0:
		print "neutral tone/emotion for %s. Count = %s"%(f, h)
	else:
		print "negative tone/emotion for %s. Count = %s"%(f, h)

if __name__ == '__main__':
	main()
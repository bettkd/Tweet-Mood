import sqlite3

conn = sqlite3.connect('tweets.db')

c = conn.cursor()

query = 'SELECT tweets FROM obama'
c.execute(query)
tweets = c.fetchall()


positiveWords = []
negativeWords = []

def loadWords(file1, file2):
	positiveWords.extend(open(file1, 'r').read().split())
	negativeWords.extend(open(file2, 'r').read().split())
	print '\n+ve and -ve words loaded..'


def main():

	loadWords(file1='newpositiveWords.txt', file2='newnegativeWords.txt')

	print "\n## Tweets on the President ##"
	print "============================"
	twts = [None]
	twts.extend([x[0].lower().encode('utf-8') for x in tweets])
	p = determineAccuracy(twts, positiveWords, 1)
	n = determineAccuracy(twts, negativeWords, -1)
	h = p + n
	print p
	print n
	printStatus(h, "obama's tweets")


def determineAccuracy(fileF, words, heuristic):
	sentCounter = 0

	sentiments = []
	for w in words:
		#print type(w)
		for s in fileF:
			if not s:
				continue
			else:
				if w in s.split():
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
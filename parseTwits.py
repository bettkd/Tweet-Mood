import re
from re import sub
import time
import cookielib
from cookielib import CookieJar
import urllib2
from urllib2 import urlopen
import difflib
import sqlite3
import numpy as np

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

keyword = 'pope%20francis'
searchLink = 'https://twitter.com/search/realtime?q='
'''table_name = 'earth_day - change it in all queries'''

allTweets = dict()

conn = sqlite3.connect('tweets.db')

c = conn.cursor()
#c.execute('''CREATE TABLE earth_day (tweets text, currentTime real)''') #create table

def main():

	
	scrapeTweets()
	#for twt in allTweets:
	#	print twt
	#print '..........'
	print len(allTweets)


def scrapeTweets():
	currentTweets = [None] #can only parse upto 20 tweets at a time
	newTweets = [None]
	similarityWeights = [.5,.5,.5,.5,.5,.5,.5,.5,.5,.5]

	i = 0
	while i < 10000: # Loop 10,000 times unless interrupted
		try:
			sourceCode = opener.open(searchLink+keyword+'&src=hash').read()
			
			#split source by tweet-text tag
			splitSource  = re.findall(r'<p class="js-tweet-text tweet-text" lang="en".*?>(.*?)</p>', sourceCode)
			
			for eachTweet in splitSource:
				tweetr = re.sub(r'<.*?>', '', eachTweet) # get rid of tags
				tweetr = re.sub(r'&.*;', '', tweetr)
				if not tweetr in allTweets:
					tweetr = tweetr.decode('utf-8')
					allTweets[tweetr] = time.time()
					#print tweetr
					c.execute("INSERT INTO pope_francis (tweets, currentTime) VALUES (?, ?)", (tweetr, time.time()))

				########### Comparison helps detetmine how much time before next ping #####
				newTweets.append(tweetr)

			compareTweets =  difflib.SequenceMatcher(None, currentTweets, newTweets)
			tweetSimilarity = compareTweets.ratio()

			currentTweets = [None]
			for x in newTweets:
				currentTweets.append(x)
			newTweets = [None]

			print '%d Tweet Similarity = %f'%(i+1, tweetSimilarity)
			similarityWeights.append(tweetSimilarity)
			similarityWeights = similarityWeights[1:]

			sleepTime = np.mean(similarityWeights)*500 # running average of the 4 wights in the array
			print '%d Sleep Time =\t     %f'%(i+1, sleepTime)

			time.sleep(sleepTime)
			##############
			conn.commit()
		except Exception, e:
			print str(e)
		i += 1
	conn.close()

if __name__ == '__main__':
	main()
	#pass


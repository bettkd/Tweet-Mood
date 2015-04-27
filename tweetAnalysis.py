import nltk
import sqlite3
import re

conn = sqlite3.connect('tweets.db')

c = conn.cursor()

ob_query = 'SELECT tweets FROM obama'
c.execute(ob_query)
ob_tweets = c.fetchall()

print ob_tweets[19]
#!/usr/bin/python

import cgi
import MySQLdb
import time

db = MySQLdb.connect(user="root",passwd="potato",db="twitterClone")
c = db.cursor()

form = cgi.FieldStorage()

user = form.getvalue("user","")
tweet = form.getvalue("tweet","")

user = cgi.escape(user)
tweet = cgi.escape(tweet)

timeStamp = time.time()

c.execute("insert into tweets(user,tweet,time) values(%s,%s,%s)", (user,tweet,timeStamp))
db.commit()

print "content-type:text/plain"
print "location: /cgi-bin/showTweets.py\n"


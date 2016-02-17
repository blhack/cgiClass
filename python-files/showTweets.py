#!/usr/bin/python

import MySQLdb
import time
import cgi

db = MySQLdb.connect(user="root",passwd="potato",db="twitterClone")
c = db.cursor()

form = cgi.FieldStorage()
user = form.getvalue("user","")

if len(user) > 0:
	c.execute("select * from tweets where user = %s order by time desc", (user))
else:
	c.execute("select * from tweets order by time desc")

results = c.fetchall()

print "content-type:text/html\n"

print "<html>"

if len(user) > 0:
	print "<h1>%s's user page</h1>" % (user)

for line in results:
	now = time.time()
	user = line[0]
	tweet = line[1]
	timeStamp = line[2]

	age = int(now-timeStamp)

	print "<a href=/cgi-bin/showTweets.py?user=%s><b>%s</b></a>" % (user,user)
	print "%s" % (tweet)
	print "<br>"
	print "%s seconds ago" % (age)
	print "<hr>"
	
print "</html>"

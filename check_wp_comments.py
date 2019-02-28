#!/usr/bin/env python2.7

#############################################################
#
# Author: Guillaume ADELINE
# Date: 15/02/2019
# Desc: Count the numbers of articles into the specific table
#
#############################################################



import sys
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="",
  passwd="",
  database="wordpress_db"
)

cursor = mydb.cursor()


cursor.execute("""
SELECT count(*) as result FROM wp_comments where comment_date between DATE_SUB(NOW(), INTERVAL 4 HOUR) and now();
	""")

row = cursor.fetchone()
print(row[0])

count = row[0]

if count < 4:
	print("OK")
	sys.exit(0)
elif count >= 4 and count < 10:
	print("WARNING")
	sys.exit(1)
elif count >= 10:
	print("CRITICAL")
	sys.exit(2)
else:
	print("UNKNOW")
	sys.exit(3)



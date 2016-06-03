# -*- coding: utf-8 -*-
import MySQLdb
import string
import sys

ID=["1887683497","2466412043","1688383542","2477971432","1748075785","2410626252","1263498570","5187664653","1751675285","1854283601","2803301701","2656274875","1826792401","2714280233","1563926367","2477339061","3217179555","1691761292","1742121542","1659041705","1549362863"]
conn=MySQLdb.connect(host='localhost',user='root',passwd='meng',db='sina',port=3306,charset='utf8')
cur=conn.cursor()
word = {}
cur.execute("create table tuijian (KeyWord varchar(255),id int)")

for each in ID:
	cur.execute("select KeyWord from a%s where KeyWord in(select KeyWord from ab%s) and type='keyword' order by num desc limit 60" % (each,each))
	for i in range(0,60):
		data  = cur.fetchone()
		word[data[0]] = each
		#print data[0],each
	for key,value in word.items():
		#print key,value
		cur.execute("insert into tuijian values('%s',%s)" % (key,value))
	word ={}
conn.commit()
cur.close()
conn.close()
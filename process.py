# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from pyltp import Segmentor,Postagger
import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
import jieba
import jieba.posseg
import jieba.analyse
import pymongo
import MySQLdb
import string
import time
import datetime

def process(str,time,tool):
	segmentor = Segmentor()
	segmentor.load("/home/meng/ltp_data/cws.model")
	words = segmentor.segment(str)
	print "|".join(words)
	segmentor.release()

	postagger = Postagger()
	postagger.load("/home/meng/ltp_data/pos.model")
	postags = postagger.postag(words)
	print "\t".join(postags)
	postagger.release()
	##关键词及其出现月份统计
	#print("分词完成")
	for i in range(len(postags)):
		if postags[i] in usefulWord:
			#print('%s %s' % (words[i], postags[i]))
			if(len(words[i]) < 4 and postags[i] != 'n'):
				a=0
			else:
				a=0	
			#	try:
			#		#print ("INSERT INTO a%s (KeyWord,num,%s,type) VALUES ('%s',1,1,'keyword') ON DUPLICATE KEY UPDATE num = num + 1,%s = %s + 1;" % (ID,month[time],words[i],month[time],month[time]));
			#		cur.execute("INSERT INTO a%s (KeyWord,num,%s,type,word) VALUES ('%s',1,1,'keyword','%s') ON DUPLICATE KEY UPDATE num = num + 1,%s = %s + 1;" % (ID,month[time],words[i],postags[i],month[time],month[time]));
			#		#conn.commit()
			#	except MySQLdb.Error,e:
			#		print "Mysql Error %d: %s" % (e.args[0], e.args[1])
	##平台统计
	#try:
	#	#print("INSERT INTO a%s (KeyWord,type,num) VALUES ('%s','tool',1) ON DUPLICATE KEY UPDATE num = num + 1;" % (ID,tool))
	#	cur.execute("INSERT INTO a%s (KeyWord,type,num) VALUES ('%s','tool',1) ON DUPLICATE KEY UPDATE num = num + 1;" % (ID,tool));		
	#	#conn.commit()
	#except MySQLdb.Error,e:
	#	print "Mysql Error %d: %s" % (e.args[0], e.args[1])
	##月份统计
	#print("update a%s set num = num + 1 where KeyWord = '%s' and type='month'" % (ID,month[time]))
	#cur.execute("update a%s set num = num + 1 where KeyWord = '%s' and type='month'" % (ID,month[time]))
	#conn.commit()	
	#print str,time,tool
	for x, w in jieba.analyse.textrank(str, withWeight=True):	
		number = float(w)
	#	cur.execute("INSERT INTO ab%s (KeyWord,num) VALUES ('%s',1) ON DUPLICATE KEY UPDATE num = num + %s;" % (ID,x,number))
		print x,w

def input(data):
	weibo_num = 0
	for word in data:
		Smonth = ''
		if(len(word['PubTime']) == 20 or len(word['PubTime']) == 19):
			Smonth = word['PubTime'][5]+word['PubTime'][6]
		elif(len(word['PubTime']) == 12 or len(word['PubTime']) == 13):
			Smonth = word['PubTime'][0]+word['PubTime'][1]
		else:
			Smonth = mon
		print(word['PubTime'],Smonth,weibo_num)
		process(word['Content'].encode("utf-8").replace("'","").replace('"',''),Smonth,word['Tools'])
		weibo_num = weibo_num + 1
		if(weibo_num % 1000 ==0):
			print("insert")
			conn.commit()		


ID = "3217179555"
month = {'01':'Jau','02':'Feb','03':'Mar','04':'Apr','05':'May','06':'June','07':'July','08':'Aug','09':'Sept','10':'Oct','11':'Nov','12':'Decm'}
mon = ''
if(time.localtime().tm_mon<10):
	mon = '0'+str(time.localtime().tm_mon)
else:
	mon = str(time.localtime().tm_mon)
try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='meng',db='sina',port=3306,charset='utf8')
    cur=conn.cursor()
    ##建表
  #  cur.execute("create table a%s (KeyWord varchar(255) primary key, type varchar(255),num int,Jau int NOT NULL DEFAULT 0,Feb int NOT NULL DEFAULT 0,Mar int  NOT NULL DEFAULT 0,Apr int NOT NULL DEFAULT 0,May int NOT NULL DEFAULT 0,June int NOT NULL DEFAULT 0,July int NOT NULL DEFAULT 0,Aug int NOT NULL DEFAULT 0,Sept int NOT NULL DEFAULT 0,Oct int NOT NULL DEFAULT 0,Nov int NOT NULL DEFAULT 0,Decm int NOT NULL DEFAULT 0,word char(255))" % (ID))
   # cur.execute("create table ab%s (KeyWord varchar(255) primary key,num double(20,12))" % (ID))
    ##给月份统计建列
   # for key,value in month.items():
    #	cur.execute("insert into a%s (KeyWord,type,num)values ('%s','month',0)" % (ID,value))
    #	conn.commit()

except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])
clinet = pymongo.MongoClient("localhost", 27017)
db = clinet["Sina"]
table = db["Tweets"]
data = table.find({"ID":ID}).batch_size(10)
usefulWord = ['b','i','j','n','nh','ni','nl','ns','nt','nz','v','ws']
input(data)
print(data.count())
conn.commit()
cur.close()
conn.close()




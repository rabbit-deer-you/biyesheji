import web
import json
from urllib import unquote

db = web.database(dbn='mysql', user='root', pw='meng', db='sina')

def get_month(id,type):
	result = {}
	data = db.query('select KeyWord,num from a%s where type="%s"' % (id,type))
	for m in data:
		result[m.KeyWord.encode("utf-8")] = int(m.num)
	return json.dumps(result)

def get_tools(id,type):
	result = {}
	n = 0
	result["others"] = int(n)
	data = db.query('select KeyWord,num from a%s where type="%s"' % (id,type))
	for m in data:
		if int(m.num) < 20:
			result["others"] = result["others"] + int(m.num)
		elif m.KeyWord.encode("utf-8") == "":
			result["others"] = result["others"] + int(m.num)
		else:
			result[m.KeyWord.encode("utf-8")] = int(m.num)
	return json.dumps(result)

def get_keyword(id,type,num):
	result = []
	#data = db.query('select KeyWord,num from %s where type="%s" order by num desc limit %s' % (id,type,num))
	data = db.query("select * from a%s where KeyWord in(select KeyWord from ab%s) and type='%s' order by num desc limit %s" % (id,id,type,num))
	for m in data:
		result.append({"key":m.KeyWord.encode("utf-8"),"value":m.num})
	return json.dumps(result)

def getkeyword_month(id,type,keyword):
	result = {}
	keyword = unquote(keyword)
	data = db.query('select * from a%s where type="%s" and KeyWord=%s' % (id,type,keyword))
	for m in data:
		result['Jau'] = int(m.Jau)
		result['Feb'] = int(m.Feb)
		result['Mar'] = int(m.Mar)
		result['Apr'] = int(m.Apr)
		result['May'] = int(m.May)
		result['June'] = int(m.June)
		result['July'] = int(m.July)
		result['Aug'] = int(m.Aug)
		result['Sept'] = int(m.Sept)
		result['Oct'] = int(m.Oct)
		result['Nov'] = int(m.Nov)
		result['Decm'] = int(m.Decm)
	return json.dumps(result)

def getsimilar(id,keyword):
	result = []
	keyword = unquote(keyword)
	data  = db.query('select * from tuijian where KeyWord = %s and tuijian.id not in ("%s")' % (keyword,id))
	for m in data:
		result.append(m.id)
	return json.dumps(result)
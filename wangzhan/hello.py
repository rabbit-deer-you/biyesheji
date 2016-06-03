import web
import model

urls = (
  '/getMonth', 'getmonth',
  '/getTools','gettools',
  '/getKeyword','getkeyword',
  '/getkeyword_month','getkeyword_month',
  '/getsimilar_user','getsimilar_user',
  '/user','user',
  '/index','index'
      )

render = web.template.render('templates')  

class index:
	def GET(self):
		return render.index(render.header(),render.footer());

class user:
	def GET(self):
		i = web.input()
		id = i.id
		return render.user(render.header(),render.footer(),id);



class getmonth:
	def GET(self):
		i = web.input()
		result = model.get_tools(i.id,i.type)
      		return result

class gettools:
	def GET(self):
		i = web.input()
		result = model.get_tools(i.id,i.type)
      		return result

class getkeyword:
	def GET(self):
		i = web.input()
		result = model.get_keyword(i.id,i.type,i.num)
      		return result

class getkeyword_month:
	def GET(self):
		i = web.input()
		result = model.getkeyword_month(i.id,i.type,i.keyword)
      		return result

class getsimilar_user:
	def GET(self):
		i = web.input()
		result = model.getsimilar(i.id,i.keyword)
      		return result

if __name__ == '__main__':  
	app = web.application(urls, globals()) 
	app.run()  

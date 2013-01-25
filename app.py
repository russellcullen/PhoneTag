import tornado.ioloop
import tornado.web
import os
from gcm import GCM

gcm = GCM('AIzaSyABIlZS0Ad_hG2CC4tjotYg2NMMZQqKI-o')
#reg_ids = ['APA91bHvDOBt0dhVzhHxBJ9D6OQfxNPqVpe4EGNogU5uWNWo1n9MJVMhRmdKXD73XtmbgvJ-9TeTz6g1CA28HnE55VlhGIY5jtIp4HWKCdnVC42Nvv3XfXILZMtGOtEm8d-iH5L1LOjPMZc4Gg0ej4LjKHIfsqM3ExmJita3LYhF6-RevbbJ828'] # Should save this on disk, not here. 
reg_ids = ['12']


class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write(reg_ids[len(reg_ids)-1])

class RegisterHandler(tornado.web.RequestHandler):
	def get(self):
		print self.get_argument('id')
		reg_ids.append(self.get_argument('id'))
				

class SendHandler(tornado.web.RequestHandler):
	def get(self):
		try:
			msg = self.get_argument('msg')
		except:
			msg = "No Message"
		data = {'msg': msg}
		gcm.json_request(registration_ids=reg_ids, data=data)
		self.write("Sent: " + msg)

application = tornado.web.Application([
	(r"/", MainHandler),
	(r"/register", RegisterHandler),
	(r"/send", SendHandler)
])

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	application.listen(port)
	tornado.ioloop.IOLoop.instance().start()

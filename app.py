import tornado.ioloop
import tornado.web
import os
from gcm import GCM

gcm = GCM('AIzaSyABIlZS0Ad_hG2CC4tjotYg2NMMZQqKI-o')
data = {'msg': 'WOWWW'}
reg_ids = ['APA91bHvDOBt0dhVzhHxBJ9D6OQfxNPqVpe4EGNogU5uWNWo1n9MJVMhRmdKXD73XtmbgvJ-9TeTz6g1CA28HnE55VlhGIY5jtIp4HWKCdnVC42Nvv3XfXILZMtGOtEm8d-iH5L1LOjPMZc4Gg0ej4LjKHIfsqM3ExmJita3LYhF6-RevbbJ828'] # Should save this on disk, not here. 

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		gcm.json_request(registration_ids=reg_ids, data=data)
		self.write("Hello World")

	def post(self):
		reg_ids.append(self.get_argument('id'))

application = tornado.web.Application([
	(r"/", MainHandler)
])

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	application.listen(port)
	tornado.ioloop.IOLoop.instance().start()

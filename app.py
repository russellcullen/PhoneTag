import tornado.ioloop
import tornado.web
import os
from gcm import GCM

gcm = GCM('AIzaSyABIlZS0Ad_hG2CC4tjotYg2NMMZQqKI-o')


class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("Hi Universe")


application = tornado.web.Application([
	(r"/", MainHandler)
])

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	application.listen(port)
	tornado.ioloop.IOLoop.instance().start()

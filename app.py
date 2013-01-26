import tornado.ioloop
import tornado.web
import os
import urlparse
#from gcm import GCM

#gcm = GCM('AIzaSyABIlZS0Ad_hG2CC4tjotYg2NMMZQqKI-o')


#from urlparse import urlparse
# query_components = { "imsi" : "Hello" }

# Or use the parse_qs method
#from urlparse import urlparse, parse_qs
#query_components = parse_qs(urlparse(self.path).query)
#imsi = query_components["imsi"] 




class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hi Universe")

class StoryHandler(tornado.web.RequestHandler):
    def get(self, story_id):
        self.write("You requested the story " + story_id)

class StoryHandler2(tornado.web.RequestHandler):
    def get(self, story_id, id_2):
        self.write("You requested the story " + story_id + " " + id_2)

class StoryHandler3(tornado.web.RequestHandler):
    def get(self):
        #print self.__dict__
        x = self.__dict__["request"]
        print x.uri
        a = x.uri.find("?") + 1
        query = x.uri[a:]
        query_components = dict(qc.split("=") for qc in query.split("&"))
        print query_components


application = tornado.web.Application([
                (r"/", MainHandler),
                (r"/story/([0-9]+)", StoryHandler),
                (r"/story/([0-9]+)/apple/([0-9]+)", StoryHandler2),
                (r"/newUser?", StoryHandler3),
            ])


if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	application.listen(port)
	tornado.ioloop.IOLoop.instance().start()

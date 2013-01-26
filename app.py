import tornado.ioloop
import tornado.web
import os
import urlparse
#from gcm import GCM

#gcm = GCM('AIzaSyABIlZS0Ad_hG2CC4tjotYg2NMMZQqKI-o')


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hi Universe")

class StoryHandler(tornado.web.RequestHandler):
    def get(self, story_id):
        self.write("You requested the story " + story_id)

class StoryHandler2(tornado.web.RequestHandler):
    def get(self, story_id, id_2):
        self.write("You requested the story " + story_id + " " + id_2)


class GetHandler(tornado.web.RequestHandler):
    def get(self):
        x = self.__dict__["request"]

        loc = x.uri.find("?")
        dbCall = x.uri[1:loc]
        query = x.uri[loc+1:]
        query_components = dict(qc.split("=") for qc in query.split("&"))
        print query_components
        
        if (dbCall == "newUser"):
            print "Calling new user to database"
        elif (dbCall == "updateUser"):
            print "Calling update user to database"

#class NewUserGetHandler(tornado.web.RequestHandler):
#    def get(self):
#        x = self.__dict__["request"]
#        a = x.uri.find("?") + 1
#        query = x.uri[a:]
#        query_components = dict(qc.split("=") for qc in query.split("&"))
#        print query_components

#class UpdateUserGetHandler(tornado.web.RequestHandler):
#    def get(self):
#       print self.__dict__
#       x = self.__dict__["request"]
#       print x.uri
#        a = x.uri.find("?") + 1
#        query = x.uri[a:]
#        query_components = dict(qc.split("=") for qc in query.split("&"))
#        print query_components


application = tornado.web.Application([
                                       #(r"/", MainHandler),
                                       #(r"/story/([0-9]+)", StoryHandler),
                                       #(r"/story/([0-9]+)/apple/([0-9]+)", StoryHandler2),
                (r"/newUser?", GetHandler),
                (r"/updateUser?", GetHandler),
            ])


if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	application.listen(port)
	tornado.ioloop.IOLoop.instance().start()

import tornado.ioloop
import tornado.web
import os
import json
from gcm import GCM
from database_api import *

gcm = GCM('AIzaSyABIlZS0Ad_hG2CC4tjotYg2NMMZQqKI-o')

db = DatabaseAPI()

class MainHandler(tornado.web.RequestHandler):
	def get(self):
    self.write("Hi Universe")

    def sendIt(gameID):
        game = db.getGameByName(gameID)
        it = game.it
        user = db.getUserByPhoneID(it)
        u = game.users
        reg_ids = []
        for x in xrange(len(u)):
            reg_ids.append(u[x].phoneID)
        data = {"it": json.dumps(user.__dict__)}
        response = gcm.json_request(registration_ids=reg_ids, data=data)
    
    def sendUserInfo(gameID, reg_id):
        l = db.getUsersByGame(gameID)
        data = {}
        
        for x in xrange(len(l)):
            temp = l[x].__dict__
            data[temp["phoneID"]] = json.dumps(temp)
        gcm.plaintext_request(registration_id=reg_id, data=data)
            


application = tornado.web.Application([
	(r"/", MainHandler)
])

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	application.listen(port)
	tornado.ioloop.IOLoop.instance().start()

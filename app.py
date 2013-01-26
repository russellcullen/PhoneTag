import tornado.ioloop
import tornado.web
import os
import urlparse
import database_api
import logging
import time
from bson.json_util import dumps
import json
#from gcm import GCM
import gcm_api
import helpers



#gcm = GCM('AIzaSyABIlZS0Ad_hG2CC4tjotYg2NMMZQqKI-o')
databaseName = 'test'

#logging.basicConfig(filename='server.log',level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)

def hash(val):
    return "YOLOSWAG_"+val


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hi Universe")

class UserGetHandler(tornado.web.RequestHandler):
    
    def get(self):
        logging.debug("In User Get Handler")
        x = self.__dict__["request"]
        loc = x.uri.find("?")
        dbCall = x.uri[1:loc]
        query = x.uri[loc+1:]
        query_components = dict(qc.split("=") for qc in query.split("&"))
        
        pID = query_components.get("phoneID")
        tkn = query_components.get("token")
        
        DB = database_api.DatabaseApi(databaseName)
        
        #no hashkey
        #newUser?phoneID=&name=
        if (dbCall == "newUser"):
            logging.info("Calling newUser")
            succ = DB.newUser(query_components)
            
            if (succ == None):
                logging.warning("Fail Call newUser")
                self.write("FailToWrite")
            else:
                logging.info("Success Call newUser: " + query_components.get("name"))
                token = hash(pID)
                self.write(token)
        
        #requires hashkey
        #updateUser?phoneID=&token=&latitude=&longitude=
        elif (dbCall == "updateUser"):
            logging.info("Calling updateUser: " + pID)
            if (tkn == hash(pID)):
                succ = DB.updateUser(query_components)
                if (succ):
                    logging.info("Success updateUser")
                    self.write("UpdateSuccess")
                else:
                    logging.warning("Fail updateUser")
                    self.write("FailToUpdate")
            else:
                logging.error("Fail updateUser -- Token did not match user. Error!")
                logging.error("PhoneID is: " + pID)
                logging.error("Token is: " + tkn)
                self.write("FailIncorrectToken")
    

class GameGetHandler(tornado.web.RequestHandler):
    
    def get(self):
        logging.debug("In Game Get Handler")
        x = self.__dict__["request"]
        loc = x.uri.find("?")
        dbCall = x.uri[1:loc]
        query = x.uri[loc+1:]
        query_components = dict(qc.split("=") for qc in query.split("&"))
        
        
        pID = query_components.get("phoneID")
        tkn = query_components.get("token")
        gnm = query_components.get("gameName")
        query_components["name"] = gnm
        
        DB = database_api.DatabaseApi(databaseName)
        
        #no hashkey
        #newGame?phoneID=&gameName=&token=
        #return on success: json(game)
        if (dbCall == "newGame"):
            logging.info("Calling newGame")
            succ = DB.newGame(pID, query_components)
            if (tkn == hash(pID)):
                if (succ == None):
                    logging.warning("Fail Call newGame")
                    self.write("FailToWrite")
                else:
                    logging.info("Success Call newGame: " + gnm)
                    self.write(dumps(succ.__dict__)) #write the JSON DUMP
            else:
                logging.error("Fail newGame -- Token did not match user. Error!")
                logging.error("PhoneID is: " + pID)
                logging.error("Token is: " + tkn)
                self.write("FailIncorrectToken")
        
        #requires hashkey
        #joinGame?token=&phoneID=&gameName=
        #return on success: json(game)
        elif (dbCall == "joinGame"):
            logging.info("Calling joinGame: " + pID)
            if (tkn == hash(pID) and gnm != None):
                succ = DB.addUserToGame(pID, gnm)
                if (succ):
                    logging.info("Success joinGame")
                    gameObj = DB.getGameByName(gnm)
                    gcm_api.alertPlayerJoined(gnm, pID)
                    self.write(dumps(gameObj.__dict__))
                else:
                    logging.warning("Fail joinGame")
                    self.write("FailToUpdate")
            else:
                logging.error("Fail joinGame -- Token did not match user or Null Game. Error!")
                logging.error("PhoneID is: " + pID)
                logging.error("Token is: " + tkn)
                self.write("FailIncorrectToken")


        #requires hashkey
        #tag?token=&phoneID&gameName=&tagName
        #return on success: none necessary
        elif (dbCall == "tag"):
            logging.info("Calling tag: " + pID)
            if (tkn == hash(pID) and gnm != None):
                succ = DB.getUserByName(query_components.get("tagName"))
                if (succ != None):
                    d = {"name" : gnm, "it" : succ.phoneID}
                    logging.info("Success tag")
                    succUpdate = DB.updateGame(d)
                    if (succUpdate):
                        helpers.changeScoreOnTag(gnm, time.time(), pID)
                        gcm_api.sendIt(gnm)
                    self.write(repr(x))
            else:
                logging.warning("Fail joinGame")
                self.write("FailToUpdate")
        else:
            logging.error("Fail joinGame -- Token did not match user or Null Game. Error!")
            logging.error("PhoneID is: " + pID)
            logging.error("Token is: " + tkn)
            self.write("FailIncorrectToken")

        #requires hashkey
        #elif (dbCall == "removeUser"):
            #logging.info("Calling remove user from database")


class ClearDataHandler(tornado.web.RequestHandler):
    
    def get(self):
        logging.debug("Clearing Data Handler")
        DB = database_api.DatabaseApi(databaseName)
        DB.clear_db()

application = tornado.web.Application([
                (r"/", MainHandler),
                (r"/newUser?", UserGetHandler),
                (r"/updateUser?", UserGetHandler),
                (r"/removeUser?", UserGetHandler),
                (r"/newGame?", GameGetHandler),
                (r"/joinGame?", GameGetHandler),
                (r"/tag?", GameGetHandler),
                (r"/clear", ClearDataHandler),
            ])

if __name__ == "__main__":
    t = gcm_api.UpdateThread()
    t.start()
    port = int(os.environ.get('PORT', 5000))
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()
    




#def sendResponseToPhone(self, phoneID):
    #token = hash(phoneID)




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


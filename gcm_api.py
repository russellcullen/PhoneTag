import game 
import user
import json
import threading
import time
from database_api import *
from gcm import GCM

gcm = GCM('AIzaSyABIlZS0Ad_hG2CC4tjotYg2NMMZQqKI-o')

rs_id = "APA91bFR9xxnyzhn_HKzLK95oHcERX8q1XVGA0AjIxHYyPU8apoKQQy7AENbsK__8jIhJCEX-Jj4Rf49c4dF3yL-2PVehg2pW44PZQDUgnDZi8mRBL0P5eVV8PgjCttWn-xDnRfOJiBOPyZMoSdXxdgf4TjY57UJIg"

class UpdateThread(threading.Thread): 
    def run(self):
        t = time.time()
        interval = 60
        while(True):
            if (time.time() > t + interval ):
                sendUserInfoAll()
                t = time.time()
                

def sendIt(gameID):
    
    db = DatabaseApi("test")
    game = db.getGameByName(gameID)
    it = game.it
    print it
    user = db.getUserByPhoneID(it)
    print user
    u = game.users
    reg_ids = []
    for x in xrange(len(u)):
        reg_ids.append(u[x])
    data = {"it": json.dumps(user.__dict__)}
    print data
    print reg_ids
    response = gcm.json_request(registration_ids=reg_ids, data=data)

def sendUserInfoAll():
    db = DatabaseApi('test')
    games = db.getAllUnfinishedGames()
    for x in games:
        a = []
        users = []
        l = db.getUsersByGame(x.name)
        data = {}
        for z in xrange(len(l)):
            user = db.getUserByPhoneID(l[z])
            a.append(user.__dict__)
            users.append(l[z])
            data = {'users' : json.dumps(a)}
        if (len(users) > 0):
            response = gcm.json_request(registration_ids=users, data=data)
        
        

def sendUserInfo(gameID, reg_id):
    
    db = DatabaseApi("test")
    l = db.getUsersByGame(gameID)
    a = []
    data = {}
    for x in xrange(len(l)):
        u = db.getUserByPhoneID(l[x])
        a.append(u.__dict__)
        '''temp = u.__dict__
        data[temp["phoneID"]] = json.dumps(temp)'''
    data = {'users' : json.dumps(a)}
    gcm.plaintext_request(registration_id=reg_id, data=data)

t = UpdateThread()
t.start()
    
#sendUserInfoAll()
#sendIt("game2")
#sendUserInfo("game2", rs_id)

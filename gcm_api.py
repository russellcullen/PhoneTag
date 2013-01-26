import game 
import user
import json
import threading
import time
from helpers import *
from database_api import *
from gcm import GCM

gcm = GCM('AIzaSyABIlZS0Ad_hG2CC4tjotYg2NMMZQqKI-o')

rs_id = "APA91bFg0W13FKARHpS0vLNkbf8eoKK4pAubK2xt-6W4TD9lxuWM0G8i8hSiQ5x_xY-tStuMePRH_w8HcCQVLbgJXVebq3xuM69vV_bLUcq1iCwMQoCHyHjQBwGDTV571rL9wUk99w52giCEYcb8ysufrZa0r06cAg"

class UpdateThread(threading.Thread): 
    def run(self):
        t = time.time()
        interval = 10
        while(True):
            if (time.time() > t + interval):
                t = time.time()
                sendUserInfoAll()
                #updateScoresAll(t)
                #checkFinishedAll(t)
                

def sendIt(gameID):
    
    db = DatabaseApi("test")
    game = db.getGameByName(gameID)
    it = game.it
    #user = db.getUserByPhoneID(it)
    u = game.users
    reg_ids = []
    for x in xrange(len(u)):
        reg_ids.append(u[x])
    data = {"it": it, "gameID" : gameID}
    print it
    print len(reg_ids)
    response = gcm.json_request(registration_ids=reg_ids, data=data)

def sendUserInfoAll():
    db = DatabaseApi('test')
    games = db.getAllUnfinishedGames()

    a = []
    users = []

    for x in games:
        
        l = db.getUsersByGame(x.name)
        data = {}
        for z in xrange(len(l)):
            user = db.getUserByPhoneID(l[z])
            a.append(user.__dict__)
            users.append(l[z])
    data = {'users' : json.dumps(a)}
    if (len(users) > 0):
        response = gcm.json_request(registration_ids=list(set(users)), data=data)
        
        
#DEPRECATED
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
#t.start()
    
#sendUserInfoAll()
#sendIt("game2")
#sendUserInfo("game1", rs_id)

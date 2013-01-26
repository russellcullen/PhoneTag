import game 
import user
import json
import threading
import time
import operator
from helpers import *
from database_api import *
from gcm import GCM

gcm = GCM('AIzaSyABIlZS0Ad_hG2CC4tjotYg2NMMZQqKI-o')

class UpdateThread(threading.Thread): 
    def run(self):
        t = time.time()
        interval = 5
        while(True):
            if (time.time() > t + interval):
                t = time.time()
                sendUserInfoAll()
                updateScoresAll(t)
                checkFinishedAll(t)
                sendScoresAll()

def sendScoresAll():
    db = DatabaseApi()
    games = db.getAllUnfinishedGames()
    for x in games:
        a = []
        sorted_scores = sorted(x.leaderboard.iteritems(), key=operator.itemgetter(1))
        sorted_scores.reverse()
        for y in sorted_scores:
            a.append({db.getUserByPhoneID(y[0]).name : y[1]})
        u = x.users
        ids = []
        for z in xrange(len(u)):
            ids.append(u[z])
        data = {"scores" : json.dumps(a)}
        if (len(ids) > 0):
            response = gcm.json_request(registration_ids=ids, data = data)
    
def sendIt(gameID):
    
    db = DatabaseApi()
    game = db.getGameByName(gameID)
    it = game.it
    u = game.users
    reg_ids = []
    for x in xrange(len(u)):
        reg_ids.append(u[x])
    data = {"it": it, "gameID" : gameID}
    response = gcm.json_request(registration_ids=reg_ids, data=data)

def sendUserInfoAll():
    db = DatabaseApi()
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
            response = gcm.json_request(registration_ids=list(set(users)), data=data)
        
def alertPlayerJoined(gameID, phoneID):
    db = DatabaseApi()
    l = db.getUsersByGame(gameID)
    users = []
    data = {}
    for x in xrange(len(l)):
        users.append(l[x])
    data = {'gameID' : gameID, 'phoneID' : phoneID}
    if (len(users) > 0):
        response = gcm.json_request(registration_ids=users, data=data)
        
#DEPRECATED
def sendUserInfo(gameID, reg_id):
    
    db = DatabaseApi()
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

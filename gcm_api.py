
from database_api import *



def sendIt(gameID):
    
    db = DatabaseAPI()
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
    
    db = DatabaseAPI()
    l = db.getUsersByGame(gameID)
    data = {}
    
    for x in xrange(len(l)):
        temp = l[x].__dict__
        data[temp["phoneID"]] = json.dumps(temp)
    gcm.plaintext_request(registration_id=reg_id, data=data)
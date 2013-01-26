### Various Tests ###

import database_api
import user
import game


a = database_api.DatabaseApi('test')

def reset_db(apiInstance):
	# Clear previous test data
	apiInstance.clear_db()
	# insert some stuff
	insertSomeUsers(apiInstance)
	insertSomeGames(apiInstance)
	
def insertSomeUsers(apiInstance):
	user1 = {"name" : "user1", "phoneID" : "user1"}
	user2 = {"name" : "user2", "phoneID" : "user2"}
	apiInstance.newUser(user1)
	apiInstance.newUser(user2)

def insertSomeGames(apiInstance):
	game1 = {"name" : "game1"}
	game2 = {"name" : "game2"}
	apiInstance.newGame("user1", game1)
	apiInstance.newGame("user2", game2)



def testGetUserByPhoneID():
	reset_db(a)
	if a.getUserByPhoneID("user1") == None:
		return False
	return True

def testGetGameByName():
	reset_db(a)
	game1 = a.getGameByName("game1")
	if game1 == None:
		return False
	return True

def testGetUsersByGame():
	reset_db(a)
	userList2 = a.getUsersByGame("game2")
	if not (len(userList2) == 1 and userList2[0] == "user2"):
		return False
	userList1 = a.getUsersByGame("game1")
	if not (len(userList1) == 1 and userList1[0] == "user1"):
		return False 
	return True

def testAddUserToGame():
	reset_db(a)
	b = a.addUserToGame("user1", "game2")
	c = a.addUserToGame("user3", "game2")
	d = a.addUserToGame("user1", "game3")
	if b and not c and not d:
		return True
	return False

def testUpdateUser():
	reset_db(a)
	user1_dict = {"name" : "user1", "phoneID" : "user1", "latitude" : 2.0, "longitude" : 3.0}
	if not a.updateUser(user1_dict):
		return False
	u = a.getUserByPhoneID("user1")
	if u.longitude == 3.0 and u.latitude == 2.0:
		return True
	return False

def testUpdateGame():
	reset_db(a)
	game1_dict = {"name" : "game1", "users" : ["user2", "user1"]}
	if not a.updateGame(game1_dict):
		return False
	g = a.getGameByName("game1")
	if len(g.users) == 2 and g.users[0] == "user2" and g.users[1] == "user1":
		return True
	return False

def testRemoveUserFromGame():
	reset_db(a)
	if not a.removeUserFromGame("user2", "game2"):
		return False
	g = a.getGameByName("game2")
	if len(g.users) == 0:
		return True
	return False

def testGetAllUnfinishedGames():
	games = a.getAllUnfinishedGames()
	if len(games) == 2:
		return True
	return False

def test():

	a = database_api.DatabaseApi('test')
	reset_db(a)

	allUsers = a.getAllUsers()
	allGames = a.getAllGames()

	print '\nUSERS\n'
	for i in allUsers:
		print i['name']

	print '\nGAMES\n'
	for i in allGames:
		print i['name']
	print '\n'

	print "Testing Functions"

	print testGetUserByPhoneID()
	print testGetGameByName()
	print testGetUsersByGame()
	print testAddUserToGame()
	print testUpdateUser()
	print testUpdateGame()
	print testRemoveUserFromGame()
	print testGetAllUnfinishedGames()

if __name__ == "__main__":
	print test()








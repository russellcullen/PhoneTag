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
	game2 = {"name" : "game2", "users" : ["user2"]}
	apiInstance.newGame(game1)
	apiInstance.newGame(game2)





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
	if not (len(userList1) == 0):
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



	

if __name__ == "__main__":
	print test()








### Various Tests ###

import database_api
import user
import game


def reset_db(apiInstance):
	# Clear previous test data
	apiInstance.clear_db()
	# insert some stuff
	insertSomeUsers(apiInstance)
	insertSomeGames(apiInstance)
	
def insertSomeUsers(apiInstance):
	user1 = user.User(name="user1")
	user2 = user.User(name="user2")
	apiInstance.newUser(user1)
	apiInstance.newUser(user2)

def insertSomeGames(apiInstance):
	game1 = game.Game(name="game1")
	apiInstance.newGame(game1)

def test():

	a = database_api.DatabaseApi('test')
	reset_db(a)

	allUsers = a.getAllUsers()
	allGames = a.getAllGames()

	raw_input("Look up all users?")

	print '\nUSERS\n'
	for i in allUsers:
		print i['name']
	print '\n'

	raw_input("Look up all games?")

	print '\nGAMES\n'
	for i in allGames:
		print i['name']
	print '\n'

if __name__ == "__main__":
	print test()








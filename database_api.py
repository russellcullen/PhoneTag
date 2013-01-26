## Directly accesses and performs operations on the MongoDB database ##

import pymongo
import os
import game
import user

class DatabaseApi:

	def __init__(self, db = 'something'):
		self.connection = pymongo.Connection(os.environ.get('MONGOLAB_URI', None))
		self.db = self.connection[db]
	
	def newUser(self, user):
		users = self.db.users
		users.insert(user.__dict__)

	def getUserByPhoneID(self, phoneID):
		users = self.db.users
		user_dict = users.find_one({'phoneID' : phoneID})
		u = user.User()
		u.fromDict(user_dict)
		return u

	# untested
	def getUserByID(self, user_id):
		pass
		
	# untested
	def deleteUser(self, user):
		pass

	# untested
	def updateUser(self, user, something):
		pass

	def newGame(self, game):
		games = self.db.games
		games.insert(game.__dict__)

	def getGameByName(self, name):
		games = self.db.games
		game_dict = games.find_one({'name' : name})
		g = game.Game()
		g.fromDict(game_dict)
		return g

	# untested
	def updateGame(self, game, something):
		pass

	# untested
	# return : true,  if successful
	# 		   false, if unsuccessful
	def addUserToGame(self, userPhoneID, gameName):
		games = self.db.games
		game = self.getGameByName(gameName)
		if (game != None):
			users = game['users']
			for u in users:
				if u.equals(userPhoneID):
					return False
			games.update({'name : gameName'}, {'$push' : {'users' : userPhoneID}})
			return True
		return False

	# untested
	def removeUserFromGame(self, user, game):
		pass

	# untested
	# returns : a list of phoneID's, if game exists
	# 		  : an empty list, 		 if game doesn't exist
	def getUsersByGame(self, gameName):
		games = self.db.games
		game = games.find_one({'name' : gameName})
		if (game == None):
			return []
		return game['users']


	# Testing functions

	def getAllUsers(self):
		users = self.db.users
		return list(users.find())

	def getAllGames(self):
		games = self.db.games
		return list(games.find())

	def clear_db(self):
		""" Deletes all data in the database"""
		for col in self.db.collection_names():
			try:
				self.db.drop_collection(col)
			except Exception:
				pass


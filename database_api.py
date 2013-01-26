## Directly accesses and performs operations on the MongoDB database ##

import pymongo
import os
import game
import user

class DatabaseApi:

	def __init__(self, db = 'something'):
		self.connection = pymongo.Connection(os.environ.get('MONGOLAB_URI', None))
		self.db = self.connection[db]
	
	# returns : User object, if doesn't exist
	# 		  : None, 		 if user exists already
	def newUser(self, user_dict):
		users = self.db.users
		u = user.User()
		u.fromDict(user_dict)
		if self.getUserByPhoneID(u.phoneID) != None:
			return None
		users.insert(u.__dict__)
		return u

	# returns : User object, if exists
	# 		  : None, 		 if doesn't exist
	def getUserByPhoneID(self, phoneID):
		users = self.db.users
		user_dict = users.find_one({'phoneID' : phoneID})
		if user_dict == None:
			return None
		u = user.User()
		u.fromDict(user_dict)
		return u
		
	# untested
	def deleteUser(self, user):
		pass

	# untested
	def updateUser(self, userPhoneID, user_dict):
		pass

	# returns : Game object, if doesn't exist
	# 		  : None, 		 if exists already
	def newGame(self, game_dict):
		games = self.db.games
		g = game.Game()
		g.fromDict(game_dict)
		if self.getGameByName(g.name) != None:
			return None
		games.insert(g.__dict__)
		return g

	# returns : Game object, if exists
	# 		  : None,		 if doesn't exist
	def getGameByName(self, name):
		games = self.db.games
		game_dict = games.find_one({'name' : name})
		if game_dict == None:
			return None
		g = game.Game()
		g.fromDict(game_dict)
		return g

	# untested
	def updateGame(self, game, something):
		pass

	# return : true,  if successful
	# 		   false, if unsuccessful
	def addUserToGame(self, userPhoneID, gameName):
		games = self.db.games
		game = self.getGameByName(gameName)
		user = self.getUserByPhoneID(userPhoneID)
		if game != None and user != None:
			users = game.users
			for u in users:
				if u == userPhoneID:
					return False
			games.update({'name' : gameName}, {'$push' : {'users' : userPhoneID}})
			return True
		return False

	# untested
	def removeUserFromGame(self, user, game):
		pass

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


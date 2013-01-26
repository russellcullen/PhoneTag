## Directly accesses and performs operations on the MongoDB database ##

import pymongo
import os

class DatabaseApi:

	def __init__(self, db = 'something'):
		self.connection = pymongo.Connection(os.environ.get('MONGOLAB_URI', None))
		self.db = self.connection[db]
		
	def newUser(self, user):
		users = self.db.users
		users.insert(user.__dict__)

	def deleteUser(self, user):
		pass

	def updateUser(self, user, something):
		pass

	def newGame(self, game):
		games = self.db.games
		games.insert(game.__dict__)

	def updateGame(self, game, something):
		pass

	def addUserToGame(self, user, game):
		pass

	def removeUserFromGame(self, user, game):
		pass




	def getUsersByGame(self, gameID):
		pass

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


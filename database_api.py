## Directly accesses and performs operations on the MongoDB database ##

import pymongo
import os
import game
import user
import time

class DatabaseApi:

	def __init__(self, db = 'something'):
		self.connection = pymongo.Connection(os.environ.get('MONGOLAB_URI', None))
		self.db = self.connection[db]
	
	# returns : User object, if doesn't exist
	# 		  : None, 		 if user exists already
	def newUser(self, userDict):
		users = self.db.users
		u = user.User()
		u.fromDict(userDict)
		if self.getUserByPhoneID(u.phoneID) != None:
			return None
		sameNameUser = users.find_one({'name' : u.name})
		if sameNameUser != None:
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

	# returns : User object, if exists
	# 		  : None, 		 if doesn't exist
	def getUserByName(self, userName):
		users = self.db.users
		user_dict = users.find_one({'name' : userName})
		if user_dict == None:
			return None
		u = user.User()
		u.fromDict(user_dict)
		return u
		
	# untested
	def deleteUser(self, userPhoneID):
		pass

	# returns : true,  if update succeeded
	# 		  : false, if update failed
	def updateUser(self, userDict):
		users = self.db.users
		phoneID = userDict['phoneID']
		u = self.getUserByPhoneID(phoneID)
		if u == None:
			return False
		# replace old user with new user
		u.fromDict(userDict);
		users.update({'phoneID' : phoneID}, u.__dict__)
		return True

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
			# add to game's user list
			games.update({'name' : gameName}, {'$push' : {'users' : userPhoneID}})
			# add to game's scoreboard
			negativeboard = game.negativeboard
			negativeboard[userPhoneID] = time.time() - game.startTime
			games.update({'name' : gameName}, {'$set' : {'negativeboard' : negativeboard}})
			leaderboard = game.leaderboard
			leaderboard[userPhoneID] = 0
			games.update({'name' : gameName}, {'$set' : {'leaderboard' : leaderboard}})
			return True
		return False

	# returns : Game object, if doesn't exist
	# 		  : None, 		 if exists already
	def newGame(self, userPhoneID, gameDict):
		games = self.db.games
		g = game.Game()
		g.fromDict(gameDict)
		if self.getGameByName(g.name) != None:
			return None
		games.insert(g.__dict__)
		self.addUserToGame(userPhoneID, g.name)
		games.update({'name' : g.name}, {'$set' : {'it' : userPhoneID}})
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

	# returns : true,  if update succeeded
	# 		  : false, if update failed
	def updateGame(self, gameDict):
		games = self.db.games
		gameName = gameDict['name']
		g = self.getGameByName(gameName)
		if g == None:
			return False
		g.fromDict(gameDict);
		games.update({'name' : gameName}, g.__dict__)
		return True

	# returns : true,  if successful
	# 		  : false, if failed
	def removeUserFromGame(self, userPhoneID, gameName):
		games = self.db.games
		game = self.getGameByName(gameName)
		users = game.users
		for user in users:
			if user == userPhoneID:
				users.remove(user)
				games.update({'name' : gameName}, {'$set' : {'users' : users}})
				return True
			return False
		return False

	# returns : a list of phoneID's, if game exists
	# 		  : an empty list, 		 if game doesn't exist
	def getUsersByGame(self, gameName):
		games = self.db.games
		game = games.find_one({'name' : gameName})
		if (game == None):
			return []
		return game['users']

	# returns : a list of Game objects, if unfinished games exist
	# 		  : an empty list,          if all games are finished
	def getAllUnfinishedGames(self):
		games = self.db.games
		unfinishedGames = list(games.find({'finished' : False}))
		ug = []
		for gameDict in unfinishedGames:
			g = game.Game()
			g.fromDict(gameDict)
			ug.append(g)
		return ug


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


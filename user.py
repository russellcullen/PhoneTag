from baseobj import *
from game import Game

class User(BaseClass):
	def __init__(self, phoneID = "", name = "", latitude = 0.0, longitude = 0.0, friends = [], games = []):
		self.phoneID = phoneID
		self.name = name
		self.latitude = latitude
		self.longitude = longitude
		self.friends = friends
		self.games = games 

	def addFriend(self, user):
		pass

	def removeFriend(self, user):
		pass

	def joinGame(self, game):
		pass

	def leaveGame(self, game):
		pass

	def updateLocation(self, lat, lng):
		self.latitude = lat
		self.longitude = lng
		# Call to db update






from baseobj import *
from user import *

class Game(BaseClass):
	def __init__(self, name = "", users = [], it = "", finished = False, negativeboard = {}, leaderboard = {}, startTime = 0.0, timeLimit = 200.0, scoreLimit = 50, lastItTime = 0.0):
		self.name = name
		self.users = users
		self.it = it
		self.finished = finished
		self.negativeboard = negativeboard
		self.leaderboard = leaderboard
		self.startTime = startTime
		self.timeLimit = timeLimit
		self.scoreLimit = scoreLimit
		self.lastItTime = lastItTime
        

	def addUser(self, user):
		pass

	def removeUser(self, user):
		pass


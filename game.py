from baseobj import *
from user import *

class Game(BaseClass):
	def __init__(self, name = "", users = [], it = "", finished = False):
		self.name = name
		self.users = users
		self.it = it
		self.finished = finished

	def addUser(self, user):
		pass

	def removeUser(self, user):
		pass


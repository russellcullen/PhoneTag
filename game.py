from baseobj import *
from user import *

class Game(BaseClass):
	def __init__(self, name = "", users = [], it = ""):
		self.name = name
		self.users = users
		self.it = it

	def addUser(self, user):
		pass

	def removeUser(self, user):
		pass

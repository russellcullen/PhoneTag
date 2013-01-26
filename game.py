class Game(object):
    def __init__(self, name = "", users = [], it = False):
    	self.name = name
    	self.users = users
    	self.it = it

    def fromDict(self, d):
		for k,v in d.items():
			if (hasattr(self, k)):
				setattr(self, k, v)
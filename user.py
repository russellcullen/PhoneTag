class User(object):
    def __init__(self, phoneID = "", name = "", latitude = 0, longitude = 0, friends = [], games = []):
    	self.phoneID = phoneID
    	self.name = name
    	self.latitude = latitude
    	self.longitude = longitude
    	self.friends = friends
    	self.games = games 

    def fromDict(self, d):
		for k,v in d.items():
			if (hasattr(self, k)):
				setattr(self, k, v)


        

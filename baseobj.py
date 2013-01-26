class BaseClass(object):

	def fromDict(self, d):
		for k,v in d.items():
			if (hasattr(self, k)):
				setattr(self, k, v)
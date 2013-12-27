class Event:
	def __init__(self,name,place,start,end,desc):
		self.name = name
		self.place = place
		self.start = start
		self.end = end
		self.desc = desc

	def getName(self):
		return self.name

	def setName(self,newname):
		self.name = newname

	def getPlace(self):
		return self.place
class Calendar:
	def __init__(self,name):
		self.name = name
		self.eventL = []

	def getName(self):
		return self.name

	def setName(self,name):
		self.name = name

	def getEventList(self):
		return self.eventL

	def addEvent(self,ev):
		self.eventL.append(ev)

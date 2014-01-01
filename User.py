import string, random

class User:
	
	def __init__(self,uname):
		
#		inisiasi username
		tmp = []
		tmp.append(uname)
		tmp.append(self.generateRandom())
		self.name = ''.join(tmp)
		
		self.queue = ''	#queue name
		self.calL = []	#list of calendar name
		self.listenerL = []	#list of listener thread
	
	def generateRandom(self,size=10,chars=string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation):
		return ''.join(random.choice(chars) for x in range(size))
	
	def getName(self):
		return self.name
	
	def setName(self,newName):
		tmp = []
		tmp.append(newName)
		tmp.append(self.generateRandom())
		self.name = ''.join(tmp)
	
	def getQueueName(self):
		return self.queue
	
	def setQueueName(self,qname):
		self.queue = qname
	
	def getCal(self):
		return self.calL
	
	def addCal(self,calName):
		if (not self.calL.__contains__(calName)):
			self.calL.append(calName)

	def getListenerL(self):
		return self.listenerL

	def addListener(self,listener):
		self.listenerL.append(listener)
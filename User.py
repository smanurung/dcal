import string, random

class User:
	
	def __init__(self,uname):
		
#		inisiasi username
		tmp = []
		tmp.append(uname)
		tmp.append(self.generateRandom())
		self.name = ''.join(tmp)
		
		self.queue = ''	#queue name
		self.calL = []	#list of calendar object
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
	
	def addCal(self,cal):
		flag = False
		for c in self.calL:
			if c.getName() == cal.getName():
				flag = True
				break
		if flag:
			pass
		else:
			self.calL.append(cal)

	def getListenerL(self):
		return self.listenerL

	def addListener(self,listener):
		self.listenerL.append(listener)

	def hasCalendar(self,name):
		for n in self.calL:
			if n.getName() == name:
				return True
		return False

	def addEvent(self,calName,ev):
		for m in self.calL:
			if (m.getName() == calName):
				m.addEvent(ev)
				break

	def showAllEvents(self):
		for c in self.calL:
			print "***",c.getName(),"***"
			for e in c.getEventList():
				print "EVENT",e.getName()
				print "Place:",e.getPlace()
				print "Start:",e.getStart()
				print "End:",e.getEnd()
				print "Description:",e.getDesc()
				print "-----"
		print "INFO: Successfully showed all events"
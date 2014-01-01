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

	def getStart(self):
		return self.start

	def getEnd(self):
		return self.end

	def getDesc(self):
		return self.desc

	def toString(self):
		tmp = []
		tmp.append(self.name)
		tmp.append('%%')
		tmp.append(self.place)
		tmp.append('%%')
		tmp.append(self.start)
		tmp.append('%%')
		tmp.append(self.end)
		tmp.append('%%')
		tmp.append(self.desc)
		return ''.join(tmp)
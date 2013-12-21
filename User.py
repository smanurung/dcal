import string, random

class User:
	
	def __init__(self,uname):
		
#		inisiasi username
		tmp = []
		tmp.append(uname)
		tmp.append(self.generateRandom())
		self.name = ''.join(tmp)
	
	def generateRandom(self,size=10,chars=string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation):
		return ''.join(random.choice(chars) for x in range(size))
	
	def getName(self):
		return self.name
	
	def setName(self,newName):
		tmp = []
		tmp.append(newName)
		tmp.append(self.generateRandom())
		self.name = ''.join(tmp)

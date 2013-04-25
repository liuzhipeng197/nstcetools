class HiveDB:
	population=0
	def __init__(self,name):
		self.name=name
		population=population+1
		print population

	def sayHi(self):
		print 'hello',self.name

	def __del__(self):
		population-=1
		print population
 
h=HiveDB('liuzhipeng')
h.sayHi()


class wash:
	company='li'
	def __init__(self,water=10,scour=2):
		self._water=water
		self.scour=scour

	@property# 属性的包装，把方法包装成实例属性
	def water(self):
		return self._water

	@water.setter
	def water(self,water):
		if 0<water<=500:
			self._water=water
		else:
			print('set failure!')

	def set_water(self,water):
		self.water=water
		
	def set_scour(self,scour):
		self.scour=scour

	def add_water(self):
		print('add water:',self.water)
		
	def add_scour(self,scour):
		print('add scour:',self.scour)
	
	def start_wash(self):
		self.add_water()
		self.add_scour()
		print('start with...')

class washDry(wash):
	pass

	def start_wash(self):
		print('..')
		super().start_wash()
		print('.....')

if __name__ == '__main__':
	w=washDry()
	w.start_wash()
	print(w.scour,w.company)

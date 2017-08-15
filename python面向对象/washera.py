class wash:
	company='li'
	def __init__(self,water=10,scour=2):
		self._water=water
		self.scour=scour

	@staticmethod
	def spins_ml(spins):
		# print('company:',wash.company)
		return spins*0.4
# 静态方法中可以引用类属性
#类方法
	@classmethod
	def get_washer(cls,water,scour):
		return cls(water,cls.spins_ml(scour))
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

if __name__ == '__main__':
	# w=wash()
	# print(w.water)
	# w.water=123
	# print(w.water)
	# print(wash.spins_ml(8))
	w=wash.get_washer(10,9)
	w.start_wash()

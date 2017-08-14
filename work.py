class Box:
	count=0
	def __init__(self,l,w,h):
		Box.count+=1#每次实例化都要调用__init__
		self.length=l
		self.width=w
		self.height=h
		self.__volume=l*w*h

	def info(self):
		print('length:',self.length,'width:',self.width,'height:',self.height,'volume:',self.__volume)
		print('count:',Box.count)
		print('count:',Box.count) 
if __name__ == '__main__':
	box1 = Box(10,20,30) 
	box1.info()	
	box2 = Box(20,20,30) 
	box2.info()	
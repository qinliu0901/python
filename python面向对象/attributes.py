class TestCss:
	cssa='class-attribute'
	def __init__(self):
		self.a=0
		self.b=10

	def info(self):
		print('a:',self.a,'b:',self.b,'cssa:',TestCss.cssa)
	# def define_a(self)；
	# 	self.c=19

if __name__ == '__main__':
	# tc=TestCss()# 类的实例化
	# tc.info()
	# tc.color='red'
	# print(tc.color)
	# tc=TestCss()
	# tca=TestCss()
	# tc.a=100
	# tc.b=200
	# tc.info()
	# tca.info()
 	# tc=TestCss()
 	# tc.define_a()
 	# print(tc.c)
 	tc=TestCss()
 	tc.info()

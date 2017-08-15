class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,oth):
        return Point(self.x + oth.x , self.y + oth.y)

    def info(self):
        print(self.x,self.y)

# class D3Point(Point):
#     def __init__(self,x,y,z):
#         super().__init__(x,y)
#         self.z = z

#     def __add__(self,oth):
#         return D3Point(self.x + oth.x , self.y + oth.y , self.z + oth.z)

#     def info(self):
#         print(self.x,self.y,self.z)

class D3Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self,oth):
        return D3Point(self.x + oth.x , self.y + oth.y , self.z + oth.z)

    def info(self):
        print(self.x,self.y,self.z)


def myadd(a,b):
    return a + b

if __name__ == '__main__':
    myadd(Point(1,2),Point(3,4)).info()
    myadd(D3Point(1,2,3),D3Point(4,5,6)).info()

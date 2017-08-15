#同类作为参数传递
class Moveable:
    def move(self):
        print('Move...')

class MoveOnFeet(Moveable):
    def move(self):
        print("Move on Feet.")

class MoveOnWheel(Moveable):
    def move(self):
        print("Move on Wheels.")

class MoveObj:
    def set_move(self,moveable):
        self.moveable = moveable()

    def move(self):
        self.moveable.move()

class Test:
    def move(slef):
        print("I'm Fly.")

if __name__ == '__main__':
    m = MoveObj()
    m.set_move(Moveable)
    m.move()
    m.set_move(MoveOnFeet)
    m.move()
    m.set_move(MoveOnWheel)
    m.move()
    m.set_move(Test)
    m.move()
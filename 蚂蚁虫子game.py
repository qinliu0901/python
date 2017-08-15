import random

class Sprite:

    step = [-2,+2,-3,+3]

    def __init__(self,gm,point=None):
        self.gm = gm
        if point is None:
            self.point = random.randint(0,20)
        else:
            self.point = point

    def jump(self):
        astep = random.choice(Sprite.step)
        if 0 <= self.point + astep <= 20:
            self.point += astep

class Ant(Sprite):

    def __init__(self,gm,point=None):
        super().__init__(gm,point)
        self.gm.set_point('ant',self.point)

    def jump(self):
        super().jump()
        self.gm.set_point('ant',self.point)

class Worm(Sprite):

    def __init__(self,gm,point=None):
        super().__init__(gm,point)
        self.gm.set_point('worm',self.point)

    def  jump(self):
        super().jump()
        self.gm.set_point('worm',self.point)

class GameMap:
    def __init__(self):
        self.ant_point = None
        self.worm_point = None

    def catched(self):
        print('ant:',self.ant_point,'worm:',self.worm_point)
        if self.ant_point is not None and self.worm_point is not None and self.ant_point == self.worm_point:
            return True

    def set_point(self,src,point):
        if src == 'ant':
            self.ant_point = point
        if src == 'worm':
            self.worm_point = point

if __name__ == '__main__':
    gm = GameMap()
    worm = Worm(gm)
    ant = Ant(gm)
    while not gm.catched():
        worm.jump()
        ant.jump()
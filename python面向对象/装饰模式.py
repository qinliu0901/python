#装饰模式
class BeDeco:
    def be_edit_fun(self):
        print('Source fun.')

    def be_keep_fun(self):
        print('Keep fun.')

class Decorater:
    def __init__(self,dec):
        self._dec = dec()

    def be_edit_fun(self):
        print('Start...')
        self._dec.be_edit_fun()

    def be_keep_fun(self):
        self._dec.be_keep_fun()

if __name__ == '__main__':
    bd = BeDeco()
    bd.be_edit_fun()
    bd.be_keep_fun()

    dr = Decorater(BeDeco)
    dr.be_edit_fun()
    dr.be_keep_fun()
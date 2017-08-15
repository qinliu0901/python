# -*- encoding:utf-8 -*-
import time,datetime
import math
import itertools
import tkinter
import threading
#导入python中的标准库
def get_clock_step(base_pntr,long_pntr):
    pos = []
    for i in range(60):
        pos.append((base_pntr[0]+long_pntr*math.cos(i*math.pi/30),
            base_pntr[0]+long_pntr*math.sin(i*math.pi/30)))
    return pos[45:] + pos[:45]

def gen_i_pos(c_pntr,long_pntr):
    for i,p in enumerate(get_clock_step(c_pntr,long_pntr)):
        yield i,p

# 指针类
class Pointer:

    def __init__(self,c_pntr,long_pntr,cvns,scale=None,super_pntr=None,width=1,fill='black'):
        # 参数说明：
        # c_pntr: 表盘的中心坐标；
        # long_pntr: 表针长；
        # cvns: 画布引用；
        # scale: 指针行走比例；
        # super_pntr: 上级指针；
        # width: 指针粗细；
        # fill: 指针颜色；
        self.pos_iter = itertools.cycle(gen_i_pos(c_pntr,long_pntr))
        self.scale = scale
        self.cvns = cvns
        self.crrnt_pos = self.pos_iter.__next__()[1]
        self.c_pntr = c_pntr
        self.super_pntr = super_pntr
        self.id_pntr = None
        self.width = width
        self.fill = fill

    def draw(self):
        self.id_pntr = cvns.create_line(self.c_pntr,self.crrnt_pos,width=self.width,fill=self.fill)

    def walk_step(self):
        self.delete()
        self.draw()
        i,self.crrnt_pos = self.pos_iter.__next__()
        if self.super_pntr and self.scale and (i + 1) % self.scale == 0:
            self.super_pntr.walk_step()

    def delete(self):
        if self.id_pntr:
            self.cvns.delete(self.id_pntr)

    def set_start(self,steps):
        for i in range(steps-1):
            self.pos_iter.__next__()
        self.crrnt_pos = self.pos_iter.__next__()[1]

class PlateImg:

    def __init__(self,c_pntr,clock_r,cvns,img):
        self.cvns = cvns
        self.clock_r = clock_r
        self.c_pntr = c_pntr
        self.img = img
        self.pid = None
        self.draw()

    def draw(self):
        self.im = tkinter.PhotoImage(file=self.img)
        self.pid = self.cvns.create_image(self.c_pntr,image = self.im)

    def delete(self):
        if self.pid:
            self.cvns.delete(self.pid)

    def set_img(self,img):
        self.img = img
        self.delete()
        self.draw()



class InImg(PlateImg):
    def draw(self):
        x = self.c_pntr[0]
        y = self.c_pntr[0] + self.clock_r / 5
        self.im = tkinter.PhotoImage(file=self.img)
        self.pid = self.cvns.create_image(x,y,image = self.im)

class CustomPlate:
    def __init__(self,c_pntr,clock_r,cvns,imgp='platex.gif',imgi='flowersx.gif'):
        self.pi = PlateImg(c_pntr,clock_r,cvns,imgp)
        self.ii = InImg(c_pntr,clock_r,cvns,imgi)

    def set_img(self,imgp,imgi):
        self.pi.set_img(imgp)
        self.ii.set_img(imgi)

    def delete(self):
        self.pi.delete()
        self.ii.delete()


class Plate:
    
    def __init__(self,c_pntr,clock_r,cvns,long=10):
        self.pos_a = get_clock_step(c_pntr,clock_r - long)
        self.pos_b = get_clock_step(c_pntr,clock_r)
        self.cvns = cvns
        self.plates = []
        self.draw()

    def draw(self):
        for i,p in enumerate(zip(self.pos_a,self.pos_b)):
            width = 5 if (i + 1) % 5 == 0 else 3
            pid = self.cvns.create_line(*p,width=width)
            self.plates.append(pid)

    def delete(self):
        if self.plates:
            for item in self.plates:
                self.cvns.delete(item)

class MyClock:

    def __init__(self,base_pntr,clock_r,cvns):
        self.c_pntr = base_pntr
        self.clock_r = clock_r
        self.cvns = cvns
        self.plate = Plate(base_pntr,clock_r,self.cvns)
        h,m,s = self.start_time()
        self.h_pntr = Pointer(base_pntr,3 * clock_r // 5,self.cvns,width=5,fill='blue')
        self.m_pntr = Pointer(base_pntr,4 * clock_r // 5,self.cvns,12,super_pntr=self.h_pntr,width=3,fill='green')
        self.h_pntr.set_start(h * 5)
        self.m_pntr.set_start(m)
        self.h_pntr.walk_step()
        self.m_pntr.walk_step()
        self.s_pntr = Pointer(base_pntr,clock_r-5,self.cvns,60,super_pntr=self.m_pntr,fill='red')
        self.s_pntr.set_start(s)

    def chg_plate(self):
        self.plate.delete()
        if isinstance(self.plate,CustomPlate):
            self.plate = Plate(self.c_pntr,self.clock_r,self.cvns)
        else:
            self.plate = CustomPlate(self.c_pntr,self.clock_r,self.cvns)
        self.h_pntr.delete()
        self.h_pntr.draw()
        self.m_pntr.delete()
        self.m_pntr.draw()

    def set_img(self,imgp,imgi):
        if not isinstance(self.plate,CustomPlate):
            self.chg_plate()
        self.plate.set_img(imgp,imgi)

    def walk_step(self):
        self.s_pntr.walk_step()

    def start_time(self):
        crrnt_time = datetime.datetime.now()
        hour = crrnt_time.hour
        minute = crrnt_time.minute
        second = crrnt_time.second
        return hour,minute,second

class MyButton:
    def __init__(self,root,clock):
        self.clock = clock
        button = tkinter.Button(root,text = '改变表盘',command = self.chg_plate)
        button.pack()

    def chg_plate(self):
        self.clock.chg_plate()

class MyTk(tkinter.Tk):
    def quit(self):
        StartClock.looping = False
        self.quit()

class StartClock:
    looping = True
    def __init__(self,mc,root):
        self.mc = mc
        self.root = root

    def start_clock(self):
        while StartClock.looping:
            self.mc.walk_step()
            self.root.update()
            time.sleep(0.05)

if __name__ == '__main__':
    root = MyTk()
    cvns = tkinter.Canvas(root,width=400,height=400,bg='white')
    cvns.pack()
    mc = MyClock((200,200),200,cvns)
    bt = MyButton(root,mc)
    t = threading.Thread(target=StartClock(mc,root).start_clock)
    t.setDaemon(True)  #用的线程
    t.start()
    root.resizable(False, False)
    root.mainloop()

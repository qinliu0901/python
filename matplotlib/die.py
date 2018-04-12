from random import randint

"""用pygal生成可缩放的矢量文件（常用在在线方式使用图表，每个设备分辨率不一样）"""


class Die():
    """表示一个骰子的类"""

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        """返回一个位于1和骰子面数的随机值"""
        return randint(1, self.num_sides)

# -*- coding: utf-8 -*-
"""
@author: qinliu
1.用函数计算

这次我们想用函数编写计算并得到结果。我们来看看一些例子：
例如：
seven(times(five())); // must return 35
four(plus(nine())); // must return 13
eight(minus(three())); // must return 5
six(dividedBy(two())); // must return 3

2.我应该选择哪个加油站？

你必须填满你的天然气，有多个加油站，价格和距离不同。有时候开车到更远的加油站会更便宜，因为价格更便宜！ 

- 你的汽车最多可以容纳60升。
- 你需要把你的汽车装满
- 根据加油站的实际价格计算油箱中的当前燃油
记住：你还需要燃料才能开到加油站！回家的路也应该考虑！
"""

class Test:

    @staticmethod
    def assert_equals(fun, res):
        assert fun == res, 'error'

# Day 10-1
# 小密圈吴凡
def zero(f=None): return 0 if not f else f(0)
def one(f=None): return 1 if not f else f(1)
def two(f=None): return 2 if not f else f(2)
def three(f=None): return 3 if not f else f(3)
def four(f=None): return 4 if not f else f(4)
def five(f=None): return 5 if not f else f(5)
def six(f=None): return 6 if not f else f(6)
def seven(f=None): return 7 if not f else f(7)
def eight(f=None): return 8 if not f else f(8)
def nine(f=None): return 9 if not f else f(9)
def plus(y): return lambda x: x+y
def minus(y): return lambda x: x-y
def times(y): return lambda x: x*y
def divided_by(y): return lambda x: x//y if y!=0 else ValueError



"""Day 10-2 当当前油量足够开到加油站时，才加油，若测试中所有的加油站都不可到站加油，则返回None；
在所有可以加油的加油站中选取价格最低的加油站，返回它"""


def gas_station(obj, currentFuel, fuelConsumption):

    stationPrice = {}
    for i in obj:
        if currentFuel / fuelConsumption * 100 > obj[i]['distance']:
            stationPrice[i] = (60 - currentFuel + 3*fuelConsumption / 100 
                * obj[i]['distance']) * obj[i]['price']
    stationPrice = sorted(stationPrice.items(), key=lambda x: x[1])
    if stationPrice:
        return stationPrice[0][0]
    else:
        return None


if __name__ == '__main__':
    obj = {"Powerfiller": {"price": 2, "distance": 50},
           "Powerfuel": {"price": 1.5, "distance": 75}}
    currentFuel = 35
    fuelConsumption = 7.5
    Test.assert_equals(gas_station(obj, currentFuel, fuelConsumption), "Powerfuel")

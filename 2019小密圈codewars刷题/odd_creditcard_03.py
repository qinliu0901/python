# -*- coding: utf-8 -*-
"""
@author: qinliu
1.判断奇数还是偶数

创建一个函数，它以整数作为参数，对偶数返回“偶数”，对奇数返回“奇数”。

2.检查信用卡

给定一个信用卡号码，我们可以通过一些基本知识来确定发行人/供应商是谁。

完成get_issuer()将使用下面显示的值的功能来确定给定卡号的发卡机构。如果数字不匹配，则该函数应返回该字符串Unknown。

  Card Type     Begins With             Number Length
  AMEX          34 or 37                15           
  Discover      6011                    16           
  Mastercard    51, 52, 53, 54 or 55    16           
  VISA          4                       13 or 16
"""

# 自己的版本

######### 1
# def even_or_odd(number):
# 	return 'Even' if number % 2 == 0 else 'Odd'

# if __name__ == "__main__":
#     print(even_or_odd(2))

######### 2
def get_issuer(number):
    st = str(number)
    return ("AMEX"       if len(st) == 15 and st[:2] in ['34', '37'] else
            "Discover"   if len(st) == 16 and st[:4] == '6011' else
            "Mastercard" if len(st) == 16 and st[0] =='5' and st[1] =='12345' else
            "VISA"       if len(st) in [13, 16] and st[0] == '4' else
            "Unknown")

 
if __name__ == "__main__":
    print(get_issuer(4111111111111111))
    print(get_issuer(378282246310005)) 
    print(get_issuer(9111111111111111))
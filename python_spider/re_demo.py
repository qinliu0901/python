#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
def re_demo():
    #解析价格
    txt = 'if you purchase more than 100 sets, the price of product A is $9.99.'
    #解析数量和价格：pattern、string、matchobjects
    #\d表示数字，+表示连接，.*表示0到多个字符，\$表示匹配美元，$是保留字，\.也是保留字
    m = re.search(r'(\d+).*\$(\d+\.?\d*)',txt)
    print(m.groups())

def re_metho():
    # search vs. match
    s = 'abcd'
    print(re.search(r'c',s))
    print(re.search(r'^c',s))#开头字符为c的

    print(re.match(r'c',s))#只能匹配开头字符为c的
    print(re.match(r'.*c',s))

def re_method():

    s1 = 'this is angel'
    s2 = 'if you purchase more than 100 sets, the price of product A is $9.99.'
    print(re.findall(r'\w+',s1))#\w为单词或字符，找出所有的
    print(re.findall(r'\d+\.?\d*',s2))

# sub 为替换
# caret ^ 表示字符串的开始，加上re.MULTILLINE多行的开始
# $ 表示一个字符串的结束，加上re.MULTILLINE多行的结束
# 转义字符\用来匹配特殊字符
# []为集合，[0-9]
def re_pattern_syntax():
    # greedy, non-greedy
    s = '<H1>title</H1>'
    print(re.match(r'<(.+)>',s).group(1))#贪婪
    print(re.match(r'<(.+?)>',s).group(1))#非贪婪,加上？



if __name__ == '__main__':
    re_pattern_syntax()
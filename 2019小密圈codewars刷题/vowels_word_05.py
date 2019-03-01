# -*- coding: utf-8 -*-
"""
@author: qinliu
1.统计元音字母

给一个字符串，统计里面的元音字母！我们给定的元音列表是:[a, e, i, o, u ] ,输入的字符串只会是小写字母或者含有空格。

2.反转字符串

编写一个函数，它接受一个或多个单词的字符串，其中里面含五个或更多字母单词必须要反转。
传入的字符串只包含字母和空格。仅当存在多个单词时才会包含空格。 

比如:s
spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test"
"""


class Test:

    @staticmethod
    def assert_equals(fun, res):
        assert fun == res, 'error'

# DAY5-1


def getCount(inputStr):
    num_vowels = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(vowels)):
        for j in range(len(inputStr)):
            if vowels[i] == inputStr[j]:
                num_vowels += 1

    return num_vowels

# leoxin
def getCount(chars):
    return len([c for c in chars if c in ['a', 'e', 'i', 'o', 'u']])


Test.assert_equals(getCount('abracadabra'), 5)


# DAY5-2
# leoxin
def spin_words(words):
    words_list = words.split()
    return ' '.join([w[::-1] if len(w) >= 5 else w for w in words_list])

assert spin_words('this is an apple') == 'this is an elppa'
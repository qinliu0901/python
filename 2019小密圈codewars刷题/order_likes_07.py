# -*- coding: utf-8 -*-
"""
@author: qinliu
1.来排个序

你的任务是对给定的字符串进行排序。字符串中的每个单词都包含一个数字。
此数字是单词在结果中应具有的位置。注意：数字可以是1到9.因此1将是第一个单词（不是0）。
如果输入字符串为空，则返回空字符串。输入String中的单词只包含有效的连续数字。

例子:
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""

2.点赞

你可能知道Facebook和其他网页上的“点赞”系统。人们可以“喜欢”博客文章，图片或其他项目
我们想要创建应该在这样的项目旁边显示的文本。实现一个函数likes :: [String] -> String。
likes [] // must be "no one likes this"
likes ["Peter"] // must be "Peter likes this"
likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"
对于4个或更多名称，数字and 2 others只会增加。
"""



def order(str):
    s = str.split()
    s.sort(key=lambda x: [int(i) for i in x if i.isdigit()])
    return ' '.join(s)
    # s.sort(key=lambda x: sorted(x)) # sorted函数对i字符串参数优先按数字排序
    # return s



def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return "%s likes this" % names[0]
        # return "arr[0] {}".format('likes this')
    elif len(names) == 2:
        return "%s and %s like this" % (names[0], names[1])
        # return "{} and {} {}".format(arr[0], arr[1], "like this")
    elif len(names) == 3:
        return "%s, %s and %s like this" % (names[0], names[1], names[2])
    else:
        return "%s, %s and %d others like this" % (names[0], names[1], len(names) - 2)

if __name__ == "__main__":

    print(order("is2 Thi1s T4est 3a"))
    print(likes(['leo', 'liu']))
    print(likes(['leo', 'liu', 'fre']))
    print(likes(['leo', 'liu', 'fre', 'zhu']))

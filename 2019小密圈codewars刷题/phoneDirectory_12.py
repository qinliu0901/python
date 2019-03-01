# -*- coding: utf-8 -*-
"""
@author: qinliu
1.电话目录

约翰将他的旧个人电话簿备份为文本文件。在文件中的每一行，他能找到的电话号码
（如格式化+X-abc-def-ghij其中X代表一个或两个数字），
与相应的名称&lt;，并&gt;和地址。

不幸的是，一切都是混合的，事情并不总是在同一个顺序; 线条的一部分混杂着非字母数字字符（电话号码和姓名除外）。

John的电话簿行示例：
"/+1-541-754-3010 156 Alphand_St. &lt;J Steeve&gt;\n"
" 133, Green, Rd. &lt;E Kustur&gt; NY-56423 ;+1-541-914-3010!\n"
"&lt;Anastasia&gt; +48-421-674-8974 Via Quirinal Roma\n"

你能帮助约翰做一个程序吗，根据他的电话簿和电话号码的行，
返回一个这个数字的字符串： "Phone =&gt; num, Name =&gt; name, Address =&gt; adress"
"""

class Test:

    @staticmethod
    def assert_equals(fun, res):
        assert fun == res, 'error'

""" Day 10-1利用正则表达式库re，返回输入的电话号码，名字，地址"""
import re


def phone(s, num):
    # 删除字符串中的多余符号,re.sub(pattern, repl, string, count=0, flags=0)
    clean = re.sub(r"[^-0-9a-z\s+A-Z<>\n.']", ' ', s)
    # 在clean中找到需匹配的电话号码，对应的一条联系人记录
    a = re.findall('.*\+' + num + '.*', clean)
    # 判断错误
    if len(a) > 1: 
        return "Error => Too many people: " + num
    if len(a) == 0: 
        return "Error => Not found: " + num
    # 在联系人记录中检索到号码并以空代替，即删除号码
    c = re.sub('\+' + num, '', a[0])
    # 检索出联系人姓名
    name = re.findall('<.*>', c)[0]
    # 先去除姓名，再检索出联系人地址,移除头尾空格
    ad = re.sub(r'\s+', ' ', re.sub(r'<.*>', '', c)).strip()
    return "Phone => " + num + ", Name => " + name[1:len(name)-1] + ", Address => " + ad

def testing(actual, expected):
    Test.assert_equals(actual, expected)


if __name__ == '__main__':
    dr = ("/+1-541-754-3010 156 Alphand_St. <J Steeve>\n 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010;\n"
		"+1-541-984-3012 <P Reed> /PO Box 530; Pollocksville, NC-28573\n :+1-321-512-2222 <Paul Dive> Sequoia Alley PQ-67209\n"
		"+1-741-984-3090 <Peter Reedgrave> _Chicago\n :+1-921-333-2222 <Anna Stevens> Haramburu_Street AA-67209\n"
		"+1-111-544-8973 <Peter Pan> LA\n +1-921-512-2222 <Wilfrid Stevens> Wild Street AA-67209\n"
		"<Peter Gone> LA ?+1-121-544-8974 \n <R Steell> Quora Street AB-47209 +1-481-512-2222!\n"
		"<Arthur Clarke> San Antonio $+1-121-504-8974 TT-45120\n <Ray Chandler> Teliman Pk. !+1-681-512-2222! AB-47209,\n"
		"<Sophia Loren> +1-421-674-8974 Bern TP-46017\n <Peter O'Brien> High Street +1-908-512-2222; CC-47209\n"
		"<Anastasia> +48-421-674-8974 Via Quirinal Roma\n <P Salinger> Main Street, +1-098-512-2222, Denver\n"
		"<C Powel> *+19-421-674-8974 Chateau des Fosses Strasbourg F-68000\n <Bernard Deltheil> +1-498-512-2222; Mount Av.  Eldorado\n"
		"+1-099-500-8000 <Peter Crush> Labrador Bd.\n +1-931-512-4855 <William Saurin> Bison Street CQ-23071\n"
		"<P Salinge> Main Street, +1-098-512-2222, Denve\n")
    testing(phone(dr, "48-421-674-8974"), "Phone => 48-421-674-8974, Name => Anastasia, Address => Via Quirinal Roma")

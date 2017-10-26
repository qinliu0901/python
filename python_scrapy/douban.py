# encoding=utf8
import requests
import re
from bs4 import BeautifulSoup
from tkinter import scrolledtext  # 导入滚动文本框的模块

from tkinter import ttk
import tkinter as tk

import threading


# 获取网页内容
def getHtml(ID):
    url = 'https://movie.douban.com/top250?start=%s&filter=' % ID
    print('url  ' + url)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2372.400 QQBrowser/9.5.10548.400'
        ,
        'Cookie': 'bid=I0klBiKF3nQ; ll="118277"; gr_user_id=ffdf2f63-ec37-49b5-99e8-0e0d28741172; ap=1; _vwo_uuid_v2=8C5B24903B1D1D3886FE478B91C5DE97|7eac18658e7fecbbf3798b88cfcf6113; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1498305874%2C%22https%3A%2F%2Fbook.douban.com%2Ftag%2F%25E9%259A%258F%25E7%25AC%2594%3Fstart%3D20%26type%3DT%22%5D; _pk_id.100001.4cf6=4e61f4192b9486a8.1485672092.5.1498306809.1498235389.; _pk_ses.100001.4cf6=*'

    }
    req = requests.get(url, headers)
    return req.text


# 解析网页并且获取相应内容
def parseHtml(html):
    # soup = BeautifulSoup(html,'lxml')   # 现在改为用正则
    print('init html.....')
    # print(html)

    # 1 取出title
    # titleRe = r'<span class="title">(.*?)</span>'
    titleRe = r'<span class="title">(.[^&]*?)</span>'  # 这里除去了副标题，（根据&nbsp 空格号进行筛选）
    regTitle = re.compile(titleRe)
    titleStr = re.findall(regTitle, html)
    # print(titleStr)
    # for verTitle in titleStr:
    #     print(verTitle)


    # 2 取出评分
    retStars = r'.*?"v:average">(.*?)</span>'
    regStars = re.compile(retStars)
    starts = re.findall(regStars, html)
    # print(starts)

    # 取出评价
    regCommend = r'<span>(.*?)</span>'
    regCommends = re.compile(regCommend)
    commends = []
    commends = re.findall(regCommends, html)
    # print(commends)
    commends.remove('·')
    commends.remove('更多')
    commends.remove('{{= year}}')
    commends.remove('{{= sub_title}}')
    commends.remove('{{= address}}')
    commends.remove('集数未知')
    commends.remove('共{{= episode}}集')
    # print(commends)

    # 取出导演，剧情（未实现）
    # regDoc= r'.*?<p class>(.*?)<br>'
    # regxDoc = re.compile(regDoc)
    # list_doc = re.findall(regxDoc,html)
    # print(list_doc)
    # print('*'*40)

    # 片言(未实现)
    # regAction = r'<p class>.*?<br>(.*?)</p>'
    # regx_action = re.compile(regAction)
    # list_action = re.findall(regx_action,html)
    # print(list_action)

    # 取出引言  希望让人自由
    regScrip = r'.*?"inq">(.*?)</span>'
    regx_scrip = re.compile(regScrip)
    list_scrip = re.findall(regx_scrip, html)
    # print(list_scrip)

    # 取出图片地址(未实现)
    # regImg = r'<div class="pic">.*?src= "(.*?)"'
    # regx_img = re.compile(regImg)
    # list_imgaddress = re.findall(regx_img,html)
    # print(list_imgaddress)

    ver_info = list(zip(titleStr, commends, list_scrip))
    return ver_info


# html = getHtml(0)
# ver_infos = parseHtml(html)
# print(ver_infos)


def write():
    print('开始爬取内容')
    ID = 0
    nums = 0
    while ID < 250:
        html = getHtml(ID)
        ver_infos = parseHtml(html)
        ID += 25
        for ver in ver_infos:
            varStr = 'No.%d\t%-30s%s\t(描述:)%-30s' % (nums, ver[0], ver[1],ver[2])
            print(varStr)
            nums += 1
            print('爬取成功'+str(nums))
def start():
    print('start  init ....')
    t1 = threading.Thread(target=write())
    t1.start()

start()
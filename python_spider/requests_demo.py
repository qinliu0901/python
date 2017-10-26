# -*- coding: utf-8 -*-
import requests

def get_json():
    r = requests.get('https://api.github.com/events')
    print(r.status_code)    #状态编码
    print(r.content)    #字节流
    print(r.headers)
    print(r.text)    #Unicode格式的文本
    print(r.json())     #应答打印成json数据

def get_querystring():
    url = 'http://httpbin.org/get'
    params = {'qs1':'value1','qs2':'value2'}  #参数,请求某网站的某几个参数
    r = requests.get(url,params=params)
    print(r.status_code)
    print(r.content)

def get_custom_headers():
    url = 'http://httpbin.org/get'
    headers = {'x-header1':'value1','x-header2':'value2'}  #参数,请求某网站的某几个参数
    r = requests.get(url,headers=headers)
    print(r.status_code)
    print(r.content)

def get_cookie():
    url = 'http://www.douban.com'
    headers = {'User-Agent':'Chrome'}   #自定义参数
    r = requests.get(url,headers=headers)
    print(r.status_code)
    print(r.cookies)
    print(r.cookies['bid'])

if __name__ == '__main__':
    get_querystring()
    get_json()
    get_cookie()
    get_custom_headers()

# -*- coding: utf-8 -*-
import requests
import urllib
import os
import threading

gImageList = [] # 访问这个全局变量是需要锁起来，acquire，release
gCondition = threading.Condition()

# producer生产者获取url，consumer消费者从这些url中下载图片下来
class Producer(threading.Thread):
    def run(self):
        global gImageList
        global gCondition
        print('%s: started' % threading.current_thread())
        imgs = download_wallpaper_list()
        gCondition.acquire()
        for i in imgs:
            if 'downloadUrl' in i:
                gImageList.append(i['downloadUrl'])
        print('%s: produce finished. Left:%s' % (threading.current_thread(),len(gImageList)))
        gCondition.notify_all()
        gCondition.release()


class Consumer(threading.Thread):
    def run(self):
        print('%s: started' % threading.current_thread())
        while True:
            global gImageList
            global gCondition

            gCondition.acquire()
            print('%s: trying to download from pool.pool size is %d' % (threading.current_thread(),len(gImageList)))
            while len(gImageList) == 0:
                gCondition.wait()
                print('%s: wake up.pool size is %d' % (threading.current_thread(),len(gImageList)))
            url = gImageList.pop()
            gCondition.release()
            _download_image(url)


def _download_image(url, folder = 'image'):
    if not os.path.isdir(folder):
        os.mkdir(folder)
    print('downloading %s' % url)

    def _fname(s):
        return os.path.join(folder, os.path.split(url)[1])
    urllib.request.urlretrieve(url, _fname(url))  #用这个函数下载图片最简单


def download_wallpaper_list():
    # 数据分析
    # http://wufazhuce.com/
    url = 'http://image.wufazhuce.com/'
    headers = {
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }
    req = urllib.request.Request(url=url, headers=headers)

    imgs = r.json()['imgs']
    print('%s: totally %d images' % (threading.current_thread(),len(imgs)))
    return imgs # 不下载，只是获取链表


if __name__ == '__main__':
    Producer().start()
    for i in range(1):
        Consumer().start()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from HTMLParser import HTMLParser

class MovieParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.movies = []
        self.in_movies = False

    def handle_starttag(self,tag,attrs):
        def _attr(attrlist,attrname):
            for attr in attrlist:
                if attr[0] == attrname:
                    return attr[1]
            return None
        print(tag)
        # 取出对应名字的值，如果属性名称与传进去的名称是一样的话，就返回属性的值，否则返回空
        if tag == 'li' and _attr(attrs,'data-title') and _attr(attrs,'data-category') == 'nowplaying':
            movie = {}
            movie['title'] = _attr(attrs,'data-title')
            movie['score'] = _attr(attrs,'data-score')
            movie['director'] = _attr(attrs,'data-director')
            movie['actors'] = _attr(attrs,'data-actors')
            self.movies.append(movie)
            print('%(title)s|%(score)s|%(director)s|%(actors)s' % movie)
            self.in_movies = True

        if tag == 'img' and self.in_movies:
            self.in_movies = False
            src = _attr(attrs,'src')
            movies = self.movies[len(self.movies) - 1]
            movie['poster-url'] = src
            _download_poster_image(movie)

def _download_poster_image(movie):
    src = movie['poster-url']
    r = requests.get(src)
    fname = src.split('/')[-1]
    with open(fname,'wb') as f:
        f.writer(r.content)
        movie['poster-path'] = fname

def nowplaying_movies(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    r = requests.get(url,headers = headers)
    parser = MovieParser()  #url解析器，继承HTMLparser
    parser.feed(r.content)  #相当于把读取的数据喂进去
    return parser.movies

if __name__ == '__main__':
    url = 'https://movie.douban.com/'
    movies = nowplaying_movies(url)

    import json
    print('%s' % json.dumps(movies,sort_keys=True,indent=4,separators=(',',':')))




# -*- coding: utf-8 -*-

from html.parser import HTMLParser
from urllib import request

class MovieParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.movies = []

    def handle_starttag(self, tag, attrs):
        def _attr(attrlist, attrname):
            for attr in attrlist:
                if attr[0] == attrname:
                    return attr[1]
            return None

        if tag == 'li' and _attr(attrs, 'data-title') and _attr(attrs, 'data-category') == 'nowplaying':
            movie = {}
            movie['title'] = _attr(attrs, 'data-title')
            movie['score'] = _attr(attrs, 'data-score')
            movie['director'] = _attr(attrs, 'data-director')
            movie['actors'] = _attr(attrs, 'data-actors')
            self.movies.append(movie)
            print('%(title)s|%(score)s|%(director)s|%(actors)s' % movie)


def nowplaying_movies(url):
    req = request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')
    s = request.urlopen(req)
    parser = MovieParser()
    # must be str, not bytes必须是字符串，不能是字节，所以需要解码，但是还是不对
    parser.feed(str(s.read()))
    return parser.movies
    


if __name__ == '__main__':
    url = 'https://movie.douban.com/cinema/nowplaying/hangzhou/'
    movies = nowplaying_movies(url)
    import json
    print('%s' % json.dumps(movies, sort_keys=True, indent=4, separators=(',', ': ')))

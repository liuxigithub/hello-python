#!/usr/bin/env python
# -*- coding:utf-8 -*-

# API key：273646050
# keyfrom：11pegasus11

'''
From:
http://www.jb51.net/article/104371.htm
'''

import json
import sys

try: # py3
    from urllib.parse import urlparse, quote, urlencode, unquote
    from urllib.request import urlopen
except: # py2
    from urllib import urlencode, quote, unquote
    from urllib2 import urlopen


def fetch(query_str=''):
    query_str = query_str.strip("'").strip('"').strip() # 删除字符串首尾的引号和空格
    if not query_str:
        query_str = 'python'

    print(query_str)
    query = {
    'q': query_str
    }
    url = 'http://fanyi.youdao.com/openapi.do?keyfrom=11pegasus11&key=273646050&type=data&doctype=json&version=1.1&' + urlencode(query)
    response = urlopen(url, timeout=3)
    html = response.read().decode('utf-8')
    return html


def parse(html):
    d = json.loads(html) # 整理返回字符串,返回的是一个dict数据
    try:
        if d.get('errorCode') == 0:
            explains = d.get('basic').get('explains')
            for i in explains:
                print(i)
        else:
            print('无法翻译')

    except:
        print('翻译出错，请输入合法单词')


def main():
    try:
        s = sys.argv[1]
    except IndexError:
        s = 'python'
    parse(fetch(s))


if __name__ == '__main__':
    main()
import re
from bs4 import BeautifulSoup
import jieba

# 书签解析器 （标题，URL，[标签]）
from ...models.Site import Site


class BookmarkParser:
    def __init__(self):
        self.__site_list = []

    def parse(self, html):
        soup = BeautifulSoup(html, 'lxml')
        elements = soup.find_all(name='a')
        for e in elements:
            if e.string is None:
                continue
            words = jieba.cut(re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……\-\·\（\）:&*（）]+", "", e.string),
                              cut_all=False)
            labels = []
            for word in words:
                if len(word) <= 1:
                    continue
                labels.append(word)
            self.__site_list.append(Site(e.string, e['href'], labels))

    def get_site_list(self):
        return self.__site_list

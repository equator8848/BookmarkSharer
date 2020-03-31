from html.parser import HTMLParser

from bs4 import BeautifulSoup


# 书签解析器
class BookmarkParser():
    def __init__(self):
        self.site_list = []

    def parse(self, html):
        soup = BeautifulSoup(html, 'lxml')
        elements = soup.find_all(name='a')
        for e in elements:
            # print(e.string, e['href'])
            self.site_list.append((e.string, e['href']))


if __name__ == '__main__':
    with open('bookmarks.html', 'r', encoding='utf-8') as bookmark:
        content = bookmark.read()
        parser = BookmarkParser()
        parser.parse(content)
        for e in parser.site_list:
            print(e)

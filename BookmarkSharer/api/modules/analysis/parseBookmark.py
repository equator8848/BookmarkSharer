from BookmarkSharer.api.modules.analysis.BookmarkParser import BookmarkParser

if __name__ == '__main__':
    with open('bookmarks.html', 'r', encoding='utf-8') as bookmark:
        content = bookmark.read()
        parser = BookmarkParser()
        parser.parse(content)
        for e in parser.get_site_list():
            print(e)

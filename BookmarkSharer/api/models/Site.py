# 站点
class Site:
    def __init__(self, title, url, labels):
        self.__title = title
        self.__url = url
        self.__labels = labels

    @property
    def get_title(self):
        return self.__title

    @property
    def get_url(self):
        return self.__url

    @property
    def get_labels(self):
        return self.__labels

    def __str__(self) -> str:
        return "Site (title=%s, url=%s, labels=%s)" % (self.__title, self.__url, self.__labels)

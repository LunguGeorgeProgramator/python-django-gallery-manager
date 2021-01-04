class Pagination:

    MAX_ON_PAGE = 50

    def __init__(self, last_page = None):
        self.__last_page = self.lastPageSetter(last_page, self.MAX_ON_PAGE)
        self.__next = self.nextSetter(self.__last_page, self.MAX_ON_PAGE)
        self.__prev = self.prevSetter(self.__last_page, self.MAX_ON_PAGE)

    @property
    def lastPage(self):
        return self.__last_page

    @property
    def next(self):
        return self.__next

    @property
    def prev(self):
        return self.__prev

    # @prev.setter
    def lastPageSetter(self, value, max_pages):
        value = int(value) if value else max_pages
        return value if value > 0 else max_pages

    # @next.setter
    def nextSetter(self, value, max_pages):
        return value + max_pages
    
    # @prev.setter
    def prevSetter(self, value, max_pages):
        prev_var = (value if value else 0) - max_pages
        return 0 if prev_var < 0 else prev_var
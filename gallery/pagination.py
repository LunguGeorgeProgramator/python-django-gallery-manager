class Pagination:

    MAX_ON_PAGE = 50

    def __init__(self, last_page = None):
        self.__last_page = int(last_page) if last_page else 0
        self.nextSetter(self.__last_page, self.MAX_ON_PAGE)
        self.prevSetter(self.__last_page, self.MAX_ON_PAGE)

    @property
    def last_page(self):
        return self.__last_page

    @property
    def next(self):
        return self.__next

    @property
    def prev(self):
        return self.__prev

    @last_page.setter
    def last_page(self):
        self.__last_page

    # @next.setter
    def nextSetter(self, value, max_pages):
        self.__next = int(int(value) + max_pages if value else max_pages)
        if self.__last_page == 0:
            self.__next = self.__next * 2
            self.__last_page = self.MAX_ON_PAGE
    
    # @prev.setter
    def prevSetter(self, value, max_pages):
        prev_var = (int(value) if value else 0) - max_pages
        self.__prev = int(0 if prev_var < 0 else prev_var)
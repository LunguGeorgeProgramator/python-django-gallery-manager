class Pagination:

    MAX_ON_PAGE = 500

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

    # @next.setter
    def nextSetter(self, value, max_pages):
        return value + max_pages

    @property
    def prev(self):
        return self.__prev

    # @prev.setter
    def lastPageSetter(self, value, max_pages):
        return int(value if value != None else max_pages)

    # @prev.setter
    def prevSetter(self, value, max_pages):
        prev_var = (value if value else 0) - max_pages
        return 0 if prev_var < 0 else prev_var

    # def setMaxPagination(max, search):
    #     return search ? max : ( >= max ? max : $this->getLastPage());
    

    # function setMinPagination($search) : int {
    #     return $search ?  0 : $this->getPrev();
    # }


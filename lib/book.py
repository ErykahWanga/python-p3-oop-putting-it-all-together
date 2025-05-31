class Book:
    def __init__(self, title, page_count, id=None):
        self._title = None
        self._page_count = None
        self.id = id
        self.title = title
        self.page_count = page_count

    def __repr__(self):
        return f"<Book {self.id}: {self.title}, {self.page_count} pages>"

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Title must be a non-empty string")
        self._title = value

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            raise ValueError("page_count must be an integer")
        if value <= 0:
            raise ValueError("page_count must be a positive integer")
        self._page_count = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
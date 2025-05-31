class Book:
    def __init__(self, title, author, page_count, id=None):
        self._title = None
        self._author = None
        self._page_count = None
        self.id = id
        self.title = title
        self.author = author
        self.page_count = page_count

    def __repr__(self):
        return f"<Book {self.id}: {self.title}, {self.author}, {self.page_count} pages>"

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Title must be a non-empty string")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Author must be a non-empty string")
        self._author = value

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Page count must be a positive integer")
        self._page_count = value
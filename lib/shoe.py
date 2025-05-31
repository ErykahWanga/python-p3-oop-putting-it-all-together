class Shoe:
    def __init__(self, brand, size, id=None):
        self._brand = None
        self._size = None
        self._condition = "New"
        self.id = id
        self.brand = brand
        self.size = size

    def __repr__(self):
        return f"<Shoe {self.id}: {self.brand}, Size {self.size}, {self.condition}>"

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Brand must be a non-empty string")
        self._brand = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
            return
        if value <= 0:
            raise ValueError("Size must be a positive integer")
        self._size = value

    @property
    def condition(self):
        return self._condition

    @condition.setter
    def condition(self, value):
        valid_conditions = ["New", "Used", "Worn"]
        if not isinstance(value, str) or value not in valid_conditions:
            raise ValueError(f"Condition must be one of {valid_conditions}")
        self._condition = value

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
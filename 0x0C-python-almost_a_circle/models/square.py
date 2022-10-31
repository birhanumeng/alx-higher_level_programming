#!/usr/bin/python3
"""In this model we create Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Define Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializing Square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Print Square iniformation in a good format."""
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """using args and kwargs"""
        if args and args != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        super().__init__(self.width,
                                         self.height, self.x,
                                         self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        super().__init__(self.width,
                                         self.height, self.x,
                                         self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Dictionary for rectangle"""
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}

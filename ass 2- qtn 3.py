class Shape:
    def __init__(self, color="black"):
        # pretend we do important setup
        self.color = color

    def calculate_area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, w, h, color="black"):
        super().__init__(color)  # call Shape.__init__
        self.w, self.h = w, h

    def calculate_area(self):
        # using Rectangle's own logic
        return self.w * self.h

rect = Rectangle(3, 5, color="blue")
print(rect.color, rect.calculate_area())
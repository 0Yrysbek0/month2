class Figure:
    unit = "cm"

    def __init__(self):
        self._perimeter = 0

    @property
    def perimeter(self):
        return self._perimeter

    @perimeter.setter
    def perimeter(self, value):
        self._perimeter = value

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def info(self):
        pass


class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self._side_length = side_length
        self.perimeter = self.calculate_perimeter()

    def calculate_area(self):
        return self._side_length ** 2

    def calculate_perimeter(self):
        return 4 * self._side_length

    def info(self):
        area = self.calculate_area()
        print(f"Square side length: {self._side_length}{Figure.unit}, perimeter: {self.perimeter}{Figure.unit}, area: {area}{Figure.unit}")


class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self._length = length
        self._width = width
        self.perimeter = self.calculate_perimeter()

    def calculate_area(self):
        return self._length * self._width

    def calculate_perimeter(self):
        return 2 * (self._length + self._width)

    def info(self):
        area = self.calculate_area()
        print(f"Rectangle length: {self._length}{Figure.unit}, width: {self._width}{Figure.unit}, perimeter: {self.perimeter}{Figure.unit}, area: {area}{Figure.unit}")


# исполняемый файл
square1 = Square(5)
square2 = Square(8)

rectangle1 = Rectangle(5, 8)
rectangle2 = Rectangle(3, 10)
rectangle3 = Rectangle(4, 6)

shapes = [square1, square2, rectangle1, rectangle2, rectangle3]

for shape in shapes:
    shape.info()
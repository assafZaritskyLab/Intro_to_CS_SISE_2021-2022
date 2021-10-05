from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    def __repr__(self):
        return type(self).__name__ + '\n' \
                                     "Area: %.3f" % (self.get_area()) + '\n' \
                                                                        "Perimeter: %.3f" % (
                   self.get_perimeter()) + '\n' + \
               25 * '='


from math import pi


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return pi * self.radius * self.radius

    def get_perimeter(self):
        return 2 * pi * self.radius


class Polygon(Shape):  # todo instance Polygon(5,8)

    def __init__(self, width, height):
        self.width = width
        self.height = height


class RightTriangle(Polygon):

    def __init__(self, width, height):
        super().__init__(width, height)
        # Polygon.__init__(self, width, height)

    def get_area(self):
        return self.width * self.height / 2

    def get_perimeter(self):
        return self.width + self.height + (self.width ** 2 + self.height ** 2) ** 0.5

class Rectangle(Polygon):

    def __init__(self, width, height):
        super().__init__(width, height)

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height


class Square(Rectangle):

    def __init__(self, width):
        Rectangle.__init__(self, width, width)


class ShapesContainer:

    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def get_total_areas(self):
        area = 0
        for shape in self.shapes:
            area += shape.get_area()    # todo it's ok??

        return area

    def __repr__(self):
        s = ''
        for shape in self.shapes:
            s = s + str(shape) + '\n'
        return s.strip()


container = ShapesContainer()
container.add_shape(Square(10))
container.add_shape(RightTriangle(8, 4))
container.add_shape(Circle(7))
container.add_shape(Rectangle(6, 4))
container.get_total_areas()

print(container)


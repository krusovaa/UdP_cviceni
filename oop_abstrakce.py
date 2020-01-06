from abc import ABC, abstractmethod


class AGO(ABC):

    def __init__(self, level_=0, color_=0):
        self.__level = level_
        self.__color = color_

    @property  # nahrazeni getteru
    def level(self):
        return self.__level

    @property
    def color(self):
        return self.__color

    @level.setter  # nahrazeni setteru
    def level(self, level_):
        self.__level = level_

    @color.setter
    def color(self, color_):
        self.__color = color_

    @abstractmethod
    def print(self):  # preddefinovana metody print
        pass


class Point(AGO):

    counter = 0

    def __init__(self, level_=0, color_=0, x_=0, y_=0, z_=0):
        super().__init__(level_, color_)  # volani konstruktu rodicovske tridy
        self.__pointID = Point.counter
        self.__x = x_
        self.__y = y_
        self.__z = z_
        Point.counter = Point.counter + 1

    def print(self):
        super().print()
        print(self.__pointID, self.__x, self.__y, self.__z)

    def __lt__(self, other):
        return self.__x < other.__x


class Ellipse:

    def __init__(self, a_=0, b_=0):
        self.__a = a_
        self.__b = b_

    def print(self):
        print(self.__a, self.__b)

    def change(self, a_, b_):
        self.__a = a_
        self.__b = b_


class Circle(Ellipse):

    def __init__(self, r_):
        super().__init__(r_, r_)

    def change(self, a_, b_):
        if a_ == b_:
            super().change(a_, b_)
        else:
            print('Error')


e = Ellipse(10, 5)
e.change(45, 12)
e.print()

c = Circle(8)
c.change(7, 7)
c.print()


p = Point(0, 0, 10, 10, 10)
q = Point(0, 0, 20, 10, 10)
print(p<q)

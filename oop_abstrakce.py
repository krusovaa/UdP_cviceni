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

    def print(self):  # preddefinovana metody print
        print(self.__level, self.__color)


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


go = AGO(1, 1)
go.print()
g = Point(0, 0, 10, 10, 10)
g.print()

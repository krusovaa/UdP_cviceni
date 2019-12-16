class Point:
    __cnt = 0

    def __init__(self, x_=0, y_=0):
        self.__id = Point.__cnt
        self.__x = x_
        self.__y = y_
        Point.__cnt = Point.__cnt + 1

    def print(self):
        print("id = " + str(self.__id))
        print("x = " + str(self.__x))
        print("y = " + str(self.__y))
        # print(str(self.__id) + " " + str(self.__x) + " " + str(self.__y))

    def getX(self):
        return self.__x

    @property
    def x(self):
        return self.__x

    def getY(self):
        return self.__y

    @property
    def y(self):
        return self.__y

    def getXY(self):
        return self.__id, self.__x, self.__y

    def setX(self, x_):
        self.__x = x_

    @x.setter
    def x(self, x_):
        self.__x = x_

    def setY(self, y_):
        self.__y = y_


class Line:

    def __init__(self, p1_, p2_):
        self.__p1 = p1_
        self.__p2 = p2_

    def print(self):
        print('Line:')
        self.__p1.print()
        self.__p2.print()

    def length(self):
        dx = self.__p2.getX() - self.__p1.getX()
        dy = self.__p2.getY() - self.__p1.getY()
        return (dx * dx + dy * dy)**0.5


class Polygon:

    def __init__(self, *points_):
        self.__points = points_

    def print(self):
        print('Polygon')
        for p in self.__points:
            p.print()


a = Point(0, 0)
b = Point(10, 10)
c = Point(0, 10)
line = Line(a, b)
line.print()
d = line.length()
print(d)
pol = Polygon(a, b, c)
pol.print()

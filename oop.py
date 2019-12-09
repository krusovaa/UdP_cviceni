class Point:
    __cnt = 0

    def __init__(self, x_ = 0, y_ = 0):
        self.__id = Point.__cnt
        self.__x = x_
        self.__y = y_
        Point.__cnt = Point.__cnt + 1


    def print(self):
        print(str(self.__id) + " " + str(self.__x) + " " + str(self.__y))


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

class Algorithms:

    def dist(self, p1, p2):
        dx = p2.x - p1.x
        dy = p2.y - p1.y
        return (dx * dx + dy * dy)**0.5


    def mid(p1, p2):
        xmid = 0.5 * (p1.x + p2.x)
        ymid = 0.5 * (p1.y + p2.y)
        m = Point(xmid, ymid)
        return m

p1 = Point()
p2 = Point(100, 100)

# a = Algorithms()
d = Algorithms.dist(p1, p2)
mid = Algorithms.mid(p1, p2)
print(d)
print(mid)

p2.print()
p1.print()
x2 = p2.getX()
x2 = p2.getY()
id2, x2, y2 = p2.getXY()
# p1.x = 200
# p1. print()
print(x2)
p2.setX(912)
p2.setY(1242)
p2.print()
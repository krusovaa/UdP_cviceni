from turtle import forward, left, right, backward, speed, exitonclick
from random import randrange, uniform

def strom(length, minangle, maxangle):
    if length < 10:
        return
    na = randrange(minangle, maxangle)
    nl = uniform(0.5 * length, 0.8 * length)

    forward(length)
    left(na)

    #draw subtree
    strom(nl, 30, 70)

    right(na)
    backward(length)
    forward(length)
    right(na)

    # draw subtree
    strom(nl, 30, 70)

    left(na)
    backward(length)
    return

speed(0)
left(90)
strom(100, 30, 70)
exitonclick()
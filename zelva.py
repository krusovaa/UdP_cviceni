from turtle import forward, left, right, exitonclick, speed

# 1 ctverec (xsize, ysize=4)

# for i in range(4):
# forward(50)
# left(90)

# 2 ctvercova sit, velikost dale promennych x, y,

# for x in range(4):
# for y in range(4):
# for i in range(4):
# forward(50)
# left(90)
# forward(50)
# left(180)
# forward(200)
# left(90)
# exitonclick()

# 3 sestiuhelnik

for i in range(2):
    for i in range(6):
        for i in range(6):
            forward(50)
            left(60)
        forward(50)
        left(60)
        forward(50)
        right(60)
    right(120)
    for i in range(6):
        forward(50)
        right(60)
        forward(50)
        left(60)

exitonclick()
from random import uniform


def random_square(npoints):
    """Returns list od tuples - random points in unit square."""
    souradnice = []
    for i in range(npoints):
        x = uniform(0, 1)
        y = uniform(0, 1)
        souradnice.append([x, y])
    return(souradnice)


def circle():
    pass


random_square(5)
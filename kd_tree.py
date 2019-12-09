from point_generator import random_square, circle

N_POINTS = 100
sq = random_square(N_POINTS)


def kd_tree(points, axis):
    axis  = 'x' or 'y'

    # if len(points) = 1, only print point and return
    if len(points) == 1:
        print(points)
        return

    # sort points according to axis
    if axis == 'x':
        points.sort(key=lambda p: p[0])  # x axis, prvni clen ntice = x, pred dvojteckou je seznam par., za veci, ktery vraci
    if axis == 'y':
        points.sort(key=lambda p: p[1])  # y axis, druhy clen ntice = y

    # def sort_x(point):
    #      return point[0]
    # points.sort (key = sort.x)

    # split points to two halves
    # find and print coordinate of the middle point
    # print each half
    mid = len(points)//2
    points_0 = points[:mid+1]
    points_1 = points[mid+1:]
    print(f"Axis: {axis}, before:{points_0}, after:{points_1}")

    # recurse on each half
    if axis == 'x':
        kd_tree(points, 'y')
    if axis == 'y':
        kd_tree(points, 'x')

kd_tree(sq, 'x')
try:
    # inp = input('Enter number: ')
    # x = int(inp)
    print('Converted')
except ValueError as e:
    print('ValueError')
    print(dir(e))
    print(e)
print('Outside')

def to_int(x):
    return int(x)

def get_int():
    inp = input("Enter number: ")
    try:
        aint = to_int(inp)
    except ValueError:
        print("{} this is not an integer, assuming 0".format((inp)))
        aint = 0
    return aint

num = get_int()
print(num)
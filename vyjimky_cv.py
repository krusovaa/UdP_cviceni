def get_int_rekurze(input_str):
    x = input(input_str)
    try:
        x = int(x)
    except ValueError:
        print(input_str)
        get_int(input_str)


def get_int_jethro(input_str):
    while True:
        int_str = input(input_str)
        try:
            int_str = int(int_str)
            return int_str
        except ValueError:
            print("Nebylo zadáno celé číslo")


def get_int(input_str):
    x = input(input_str)
    while x != "":  # nebo while True
        try:
            x = int(x)
            break
        except ValueError:
            print('Not an integer')
            x = input(input_str)
    return x


num = get_int("Zadej polomer Zeme: ")
print(num)
# num_2 = get_int_rekurze("Zadej polomer Zeme: ")
# print(num_2)
# num_J = get_int_jethro("Zadej polomer Zeme: ")
# print(num_J)

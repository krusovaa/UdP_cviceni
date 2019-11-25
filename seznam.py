s = []
z = 'y'

while z != "":
    z = input("jakou polozku?")
    if z != "x":
        s.append(z)
    if z == "x":
        break
print("V seznamu je:", s)

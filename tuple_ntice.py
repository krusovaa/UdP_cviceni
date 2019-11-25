# from typing import List, Tuple

s = [ ]
polozka = 'x'
mnozstvi = 'y'

while polozka != "":
    polozka = input("jakou polozku?")
    if polozka != "x":
        mnozstvi = input("mnozstvi?")
        if mnozstvi != "":
            s.append((polozka, mnozstvi))
    if polozka == "x":
        break
print("V seznamu je:", s)
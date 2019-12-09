a1 = {"wheels": 4, "power": 30, "max_speed": 120}
a2 = {"wheels": 4, "power": 100, "max_speed": 150, "blinker": 2}
print(a1)
print(a2)
print(a1["wheels"])

# oprava slovníku
a1["wheels"] = 5
print(a1)

# vznik klíče hned, nemusíme ho nijak předem deklarovat
a1["blinker"] = 3

# blinker, max_speed, power, wheels ... klíče
if "blinker" in a1:
    print("Blinkers: ", a1["blinker"])
if "blinker" in a2:
    print("Blinkers: ", a2["blinker"])

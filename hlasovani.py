# strany
poceta = 0
pocetb = 0
pocetc = 0
pocetd = 0

# definovat promenou z
z = 'y'

# odpoved A, B, C, D
while z != "":
    z = input("Jakou stranu zvolit?")
    if z == 'a':
        poceta = poceta + 1
    if z == 'b':
        pocetb = pocetb + 1
    if z == 'c':
        pocetc = pocetc + 1
    if z == 'd':
        pocetd = pocetd + 1
    if z == 'x':
        break
print("Strana A:", poceta, "Strana B:", pocetb, "Strana C:", pocetc, "Strana D:", pocetd)
print(f"Strana A: {poceta}\nStrana B: {poceta}\nStrana C: {poceta}\nStrana D: {poceta}")

print("\"Ahoj\",řekl")

print(f"""Strana A: {poceta}
Strana B: {pocetb}""")

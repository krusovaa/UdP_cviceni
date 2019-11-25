#  DGR to DMS

a = float(input('Zadej stupně:'))

d = int(a)
m = (a - int(a))*60
s = (m - int(m))*60
m = int(m)

print("Výsledek je", end=' ')
# neodradkuje
print(d, "stupňů", m, "minut a ", s, "vteřin")

from turtle import forward, backward, left, right

def ctverecek(delka_strany):
    for i in range (4):
        forward(delka_strany)
        right(90)

a = 3
x = 3
y = 10
# Nakresli čtvercovou sít
for yi in range(y):
   # nakreslí řádek
     for xi in range(x):
         # nakreslí čtvereček
         for i in range(4):
          forward(a)
          left(90)
          # posune se o čtvereček doprava
          forward(a)
     # vrátí se na začátek
left(180)
forward(x*a)
left(180)
# posune se o řádek nahoru
left(90)
forward(a)
right(90)

left(45)
forward(100)

ctverecek(10)

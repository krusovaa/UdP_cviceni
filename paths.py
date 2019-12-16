import pathlib

p = pathlib.Path('/Users/zvukar/Desktop/B 4. ročník/Úvod do programování/cviceni/paths.py')
p2 = pathlib.Path('paths.py')
print(p)
for par in p.parents:
    print(par)
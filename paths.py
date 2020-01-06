import pathlib

p = pathlib.Path('C:/Users/zvukar/Desktop/B 4. ročník/Úvod do programování/cviceni/paths.py')
p2 = pathlib.Path('paths.py')
print(p)
for par in p.parents:
    print(par)


adir = p.parent
for file in adir.iterdir():
    if file.is_dir:
        print("Dir {}".format(file))
    else:
        print(file)
print(p.parent)

cwd = pathlib.Path.cwd()
in_dir = cwd / 'in'
for file in in_dir.iterdir():
    print(file)
    with open (file, "r", encoding="utf-8") as f:
        print(f.read())
print(in_dir)

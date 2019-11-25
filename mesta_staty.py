import random

def nacti_stat_a_hlavni_mesto(staty):
    #nactu od uzivatele stat a hlavni mesto
    #pokud je stat x vratim false
    #jinak pridam stat a mesto do seznamu staty a vratim True

    stat = input("Jaky stat: ")
    hlavni_mesto = input("Jake hlavni mesto: ")
    if stat == 'x':
        return False
    else:
        staty.append([stat,hlavni_mesto])
        return True

def nacti_staty_a_hlavni_mesta():
    # dokud uzivatel nezadal x, nacitam stat a hlavni mesto
    staty1 = [ ]
    while True:
        vysl = nacti_stat_a_hlavni_mesto(staty1)
        if not vysl:
            return staty1

def hadej_hlavni_mesto(stat,mesto):
    chyby = 0
    print(stat)
    odpoved = input("Napis hlavni mesto")
    while odpoved != mesto:
        chyby += 1
        print("spatne, napoveda je:", mesto[0:chyby])
        odpoved = input("Napis hlavni mesto")


    #dokud uzivatel nezadal spravne hlavni mesto:
    #zeptej se na hlavni mesto
    #rekni mu tolik pusmen, kolkrat uz neuhodl


def hadej_hlavni_mesta(staty3):
    pass
    random.shuffle(staty3)
    mesto = ''


    while len(staty3) > 0 and mesto != "x":
        sp = staty3.pop()
        stat = sp[0]
        mesto = sp[1]
        #lze take (stat,mesto) = sm
        #lze take (stat,mesto) = staty3.pop()
        hadej_hlavni_mesto(stat,mesto)


    #dokud uzivatel nezadal x, ptam se na hlavni mesto
    #zamichej staty
    # dokud jsou nejake staty v seznamu
    # vyzvedni dvojci stat mesto ze seznamu statu

staty2 = nacti_staty_a_hlavni_mesta()
print(staty2)
hadej_hlavni_mesta(staty2)

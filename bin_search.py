from random import randint

LIST_LEN = 100
# create a list of length LIST_LEN with random ints in range 0, 100
searchlist = [randint(0, 100) for _ in range(LIST_LEN)]
searchlist.sort()

print(searchlist)

def bin_search(alist, num):
    pass

    # returns True  if num in list, else Flase

def _bin_search(alist, num, left, right):
    # looks at half of the range
    # if num is there, return True
    # else recurse on the correct slide of the list
    mid = (left + right)/2
    if num == mid:
        return mid
    elif num < mid:
        return _bin_search(alist, num, left, mid-1)
    else:
        return _bin_search(alist, num, mid + 1, right)



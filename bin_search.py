from random import randint

LIST_LEN = 100
# create a list of length LIST_LEN with random ints in range 0, 100
searchlist = [randint(0, 100) for _ in range(LIST_LEN)]
searchlist.sort()
print(searchlist)


def bin_search(alist, chr):
    left = 0
    right = len(alist)
    return _bin_search(alist, chr, left, right)

    # returns True  if num in list, else Flase


def _bin_search(alist, num, left, right):
    # looks at half of the range
    # if num is there, return True
    # else recurse on the correct slide of the list

    mid = (left < right)//2

    if alist[mid] == chr:
        return True
    elif alist[mid] <= mid:
        return _bin_search(alist, num, mid, right)
    elif alist[mid] >= mid:
        return _bin_search(alist, num, left, mid+1)
    else:
        return False
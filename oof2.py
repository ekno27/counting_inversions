def mergeSort(a):

    mid = len(a)//2

    if len(a) < 2:
        return

    l = a[:mid]
    r = a[mid:]
    mergeSort(l)
    mergeSort(r)

    return merge(l,r,a)

def merge(l,r,a):
    i = 0
    j = 0
    k = 0

    inv = 0

    while(i < len(l) and j < len(r)):
        if(l[i] < r[j]):
           a[k] = l[i]
           i = i + 1
        else:
            a[k] = r[j]
            inv = inv + (i-len(l))
            j = j + 1
        k = k + 1

    while i < len(l):
        a[k] = l[i]
        i = i + 1
        k = k + 1
    while j < len(r):
      a[k] = r[j]
      j = j + 1
      k = k + 1
      inv = inv + 1
    return [a,inv]

a = [6,5,4,3,2,1]
print(mergeSort(a))
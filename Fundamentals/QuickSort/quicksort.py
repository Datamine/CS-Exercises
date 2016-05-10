def partition(array, lo, hi):
    pivot = array[hi]
    i = lo
    for j in range(lo, hi):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[hi] = array[hi], array[i]
    return pivot

def quicksort(array, lo, hi):
   if lo < hi:
        p = partition(array, lo, hi) 
        quicksort(array, lo, p-1)
        quicksort(array, p+1, hi)
        return array

########## TESTING #############################################################
from random import randint
for i in range(100):
    r_array = [randint(0,100) for x in range(randint(0,100))]
    if quicksort(r_array,0,len(r_array)-1) == sorted(r_array):
        continue
    else:
        print "Random Test Case " + str(i) + " Failed!"
        break
else:
    print "All Test Cases Passed!"

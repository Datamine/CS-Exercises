# this solution assumes correct (i.e. non-malicious) input. Does not detect bad input.

def invert_choose_2(x):
    # undo the n choose 2 formula and we get a quadratic to solve
    # n^2 - n - 2x = 0
    a = 1.0
    b = -1.0
    c = -2.0 * x
    quadratic_sol_1 = (-b + (b**2 - (4*a*c))**0.5) / (2*a)
    # disregard the second solution because we want the positive one
    return int(round(quadratic_sol_1))

def get_numbers(pairwise_sums):
    # note that len(pairwise_sums) == len(original list of numbers) choose 2
    # we invert the choose 2 operation to get the length of the original list
    original_len = invert_choose_2(len(pairwise_sums))

    # creating a diagonal matrix representing the pairwise sums
    pairwise_matrix = []
    current_len = original_len - 1
    while pairwise_sums != []:
        sliced = pairwise_sums[:current_len]
        pairwise_matrix.append(sliced)
        # now update pairwise_sums and shorten the next slice
        pairwise_sums = pairwise_sums[current_len:]
        current_len -=1

    # Where [x1...xn] is the original list of numbers, the diagonal matrix is:
    # x1 + x2, x1 + x3, x1 + x4, ...
    # x2 + x3, x2 + x4, ...
    # x3 + x4, ...

    # We also get to assume that there are at least 3 items. Then we use
    # arithmetic: (x1+x3) - (x2+x3) = (x1 - x2) which we compare against (x1+x2)
    # to obtain x2 and in turn x1, and from the first row, the remaining x's.

    x1_plus_x2 = pairwise_matrix[0][0]
    x1_plus_x3 = pairwise_matrix[0][1]
    x2_plus_x3 = pairwise_matrix[1][0]

    x1_minus_x2 = x1_plus_x3 - x2_plus_x3
    two_x2 = x1_plus_x2 - x1_minus_x2
    x2 = two_x2/2
    x1 = x1_plus_x2 - x2
    
    results = [x1]
    for x in pairwise_matrix[0]:
        results.append (x - x1)

    return results

############ TESTING ##########################################################

#print get_numbers([5,6,7,8,7,8,9,9,10,11])
#print get_numbers([4,4,4])

# Run a general test...

from random import randint
from itertools import combinations
for i in range(100):
    r_length = randint(3,20)
    random_ints = [randint(-50,50) for x in range(r_length)]
    pairwise_sums = [a+b for (a,b) in list(combinations(random_ints,2))]
    originals = get_numbers(pairwise_sums)
    if originals == random_ints:
        print "Random Test Case " + str(i) + " Passed!"
    else:
        print "Random Test Case " + str(i) + " Failed! <---"

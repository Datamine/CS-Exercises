"""
Goal: to write a function add(x) that takes an arbitrary number of calls, e.g.
add(3)(4)(1)() -> 8
"""

def mkadd1(acc):
    def add1(*args):
        if len(args) == 0:
            return acc
        return mkadd1(acc + args[0])
    return add1

def add(*args):
    if len(args) == 0:
        return 0
    return mkadd1(args[0])

print add(3)(4)(1)()

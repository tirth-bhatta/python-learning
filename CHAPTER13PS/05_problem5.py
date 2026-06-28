from functools import reduce
a = [111, 2, 342, 53, 385, 65, 87, 45, 55]


def greater (a, b):
    if(a>b):
        return a
    return b
print(reduce(greater, a))
#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        return sum(x * y for x, y in my_list) / sum(y for x, y in my_list)
    return 0
    # = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)

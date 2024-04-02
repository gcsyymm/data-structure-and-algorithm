from random import randint


def kandane(l):
    max_ending_here = 0
    max_so_far = -1e9
    for i in l:
        max_ending_here += i
        max_so_far = max(max_ending_here, max_so_far)
        max_ending_here = max(max_ending_here, 0)
    return max_so_far


test = [randint(-10, 10) for i in range(10)]
print(test)
print(kandane(test))

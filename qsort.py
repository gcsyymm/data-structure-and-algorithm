import random


def qsort(nums: list):
    if len(nums) < 1:
        return []
    pivot = nums[-1]
    s, l = [], []
    for num in nums[:-1]:
        if num < pivot:
            s.append(num)
        else:
            l.append(num)
    return qsort(s) + [pivot] + qsort(l)


list1 = [random.randint(1, 100) for i in range(10)]
print(list1)
print(qsort(list1))

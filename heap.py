import heapq
import random

mylist = [random.randint(0, 10) for i in range(10)]
print(mylist)
heapq.heapify(mylist)
print(mylist)
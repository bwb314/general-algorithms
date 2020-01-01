from heap import minheap
import heapq
from random import random

a = minheap()


for _ in range(10000):
    a.push(int(5000 * random()))
    #a.heap.append(int(20 * random()))

for _ in range(100):
    #print(a.poppush(int(5000 * random())))
    print(a.popmin())

b = a.heap[:]
heapq.heapify(b)
print(a.heap == b)

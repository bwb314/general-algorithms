from segment_tree import segtree
from random import random

a = [int(random()*100000) for _ in range(3000)]
print(a)

c = segtree(a, op = sum)
#c.level_order_traversal()

print(c.query(50,1299))
ans = sum(a[50:1300])
print(ans)

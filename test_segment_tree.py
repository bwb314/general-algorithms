from segment_tree import segtree
from random import random

a = [int(random()*1000) for _ in range(3000)]
#c = segtree(a, op = sum)
#
##c.level_order_traversal()
#
#myans = c.query(50,1299)
#ans = sum(a[50:1300])
#print(myans == ans)
#c.update(100, 6666)
#a[100] = 6666
#myans = c.query(50,1299)
#ans = sum(a[50:1300])
#print(myans == ans)

for op in [sum, max, min]:
    c = segtree(a, op = op)
    for i in range(1000):
        ind, val = int(random()*3000), int(random()*1000) 
        c.update(ind, val)
        a[ind] = val
        l = int(random()*1000) 
        r = min(l + int(random()*1000), 99999)
        myans = c.query(l,r)
        ans = op(a[l:r+1])
        print(l,r, myans, ans)
    


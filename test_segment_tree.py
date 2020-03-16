from segment_tree import segtree
from random import random

random_arr = [int(random()*1000) for _ in range(3000)]
    
def test_max():
    c = segtree(random_arr, op = max)
    l = int(random()*1000) 
    r = min(l + int(random()*1000), 99999)
    myans = c.query(l,r)
    correct_ans = max(random_arr[l:r+1])
    assert correct_ans == myans, "{} should be {}".format(correct_ans, myans)

def test_min():
    c = segtree(random_arr, op = min)
    l = int(random()*1000) 
    r = min(l + int(random()*1000), 99999)
    myans = c.query(l,r)
    correct_ans = min(random_arr[l:r+1])
    assert correct_ans == myans, "{} should be {}".format(correct_ans, myans)

def test_sum():
    c = segtree(random_arr, op = sum)
    l = int(random()*1000) 
    r = min(l + int(random()*1000), 99999)
    myans = c.query(l,r)
    correct_ans = sum(random_arr[l:r+1])
    assert correct_ans == myans, "{} should be {}".format(correct_ans, myans)

def test_update():
    c = segtree(random_arr, op = max)
    c.update(1797, 3141)
    random_arr[1797] = 3141
    myans = c.query(1797,1797)
    correct_ans = random_arr[1797]
    assert correct_ans == myans, "{} should be {}".format(correct_ans, myans)


#a = [int(random()*1000) for _ in range(3000)]
##c = segtree(a, op = sum)
##
###c.level_order_traversal()
##
##myans = c.query(50,1299)
##ans = sum(a[50:1300])
##print(myans == ans)
##c.update(100, 6666)
##a[100] = 6666
##myans = c.query(50,1299)
##ans = sum(a[50:1300])
##print(myans == ans)
#
#for op in [sum, max, min]:
#    c = segtree(a, op = op)
#    for i in range(1000):
#        ind, val = int(random()*3000), int(random()*1000) 
#        c.update(ind, val)
#        a[ind] = val
#        l = int(random()*1000) 
#        r = min(l + int(random()*1000), 99999)
#        myans = c.query(l,r)
#        ans = op(a[l:r+1])
#        assert ans == myans, "{} should be {}".format(ans, myans)
#        #if myans == ans:
#        #    print(l,r, myans, ans)
#
#        #else:
#        #    print("WRONG!")
#        #    raise ValueError("Yo answer wrong!")

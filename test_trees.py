from trees import tree

lines = open('input05.txt', 'r').readlines()

arr = list(map(int, lines[1].split()))
rqmtree = tree(arr)
rqmtree.form_rqm_segtree(min)
requests = lines[2:]
outputs = list(map(int,open('output05.txt' ,'r').readlines()))

ans = []

for i, request in enumerate(requests):

    l = int(request.split()[0])
    r = int(request.split()[1])
    

    na = rqmtree.rqm_query(l,r)

    ans.append([na, outputs[i]])


for i in ans:

    if i[0] != i[1]:

        print("ALERT!")

    


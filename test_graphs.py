# Test for adjacency lists
from graphs import form_adj_list

test_arr = [0,1,2,3,8,9,11,15]

def diffone(a,b):

    diff = abs(a-b)

    if diff <= 1:
        return True
    else:
        return False

adj_list = form_adj_list(test_arr, diffone)

print(adj_list)

# Answer
ans = "{0: {1}, 1: {0, 2}, 2: {1, 3}, 3: {2}, 8: {9}, 9: {8}, 11: set(),"\
        " 15: set()}"

print(ans)

from graphs import bfs

levels, parents = bfs(adj_list, 0)

ans_level = {0:0, 1:1, 2:2, 3:3}
ans_parent = {0:0, 1:0, 2:1, 3:2}

for i in [0, 1, 2, 3]:

    level = levels[i]
    parent = parents[i]

    print(level, ans_level[i],"   ", parent, ans_parent[i])

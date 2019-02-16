class tree:

    def __init__(self, array):

        self.rqm_segtree = []
        self.form_rqm_segtree(array)



    def form_rqm_segtree(self, array):


        levels = []

        level = array

        while len(level) != 1:


            if len(level)%2 == 1:

                level.append('')
            
            levels.append(level)


            next_level = []


            for i in range(len(level)//2):

                l = level[2*i]
                r = level[2*i + 1]

                if r == '':
                
                    next_level.append(l)

                else:
                
                    next_level.append(min(l,r))

            level = next_level

        levels.append(level)

        
        while levels:

            level = levels.pop()
            self.rqm_segtree += level



arr = list(range(100))

rqmtree = tree(arr)


print(rqmtree.rqm_segtree)


            

            

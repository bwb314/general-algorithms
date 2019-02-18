import math

class tree:

    def __init__(self, array):

        self.rqm_segtree = []
        self.length = len(array)
        self.form_rqm_segtree(array)



    def form_rqm_segtree(self, array):

        levels = []

        level = array
        
        height = math.log(len(level))/math.log(2)

        self.height = math.ceil(height)
        self.leaves = len(level)

        while self.leaves != 2**self.height:

            level.append('')
            self.leaves = len(level)
            height = math.log(len(level))/math.log(2)


        while level:

            levels.append(level)

            next_level = []

            for i in range(len(level)//2):

                l = level[2*i]
                r = level[2*i + 1]

                if l == '':

                    next_level.append('')

                elif r == '':
                
                    next_level.append(l)
                
                else:
                
                    next_level.append(min(l,r))

            level = next_level

        
        while levels:

            level = levels.pop()
            self.rqm_segtree += level


    def rqm_query(self, l, r):
    
    
    
        segtree = self.rqm_segtree
        
        if l > r or r >= self.length: 
    
            return "NO"
    
        new_min = ''
        
        frontier = set()

        frontier.add((0,0,self.leaves-1))
    
        while frontier:
    
            child = frontier.pop()
            ind = child[0]
            lind = child[1]
            rind = child[2]
    
            if segtree[ind] == '':
    
                continue
    
            if (rind <= r and lind >= l):
    
                if new_min == '':
    
                    new_min = segtree[ind]
    
                new_min = min(segtree[ind], new_min)
                
                continue
        
            left = 2 * ind + 1
            right = left + 1
    
            llind = lind
            lrind = lind + (rind - lind)//2
            rlind = lrind + 1
            rrind = rind
            
            if lrind == rrind:
        
                lrind = llind
                rlind = rrind
    
    
            if lrind >= l:

                frontier.add((left,llind,lrind))
           
            if rlind <= r: 
    
                frontier.add((right,rlind,rrind))
            
        return new_min



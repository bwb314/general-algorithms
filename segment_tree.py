class node:

    def __init__(self, left=None, right=None, **kwargs):

        self.left = left
        self.right = right
        self.__dict__.update(kwargs)


class segtree:

    # Default op sets up range max query
    def __init__(self, arr, op = max):

        if op not in [max, min, sum]:
            raise ValueError("Operation not supported")            
        self.op = op
        self.root = self.build(arr)
    

    def build(self, arr):
    
        frontier = [node(left = None, right = None, indl = i, indr = i, val = x) for i, x in enumerate(arr)]
        if len(frontier) == 0:
            return

        while len(frontier) != 1:

            if len(frontier)&1:
                frontier.append(None)
            for i in range(len(frontier)//2):
                left = frontier.pop(0)
                right = frontier.pop(0)
                
                if right != None:
                    frontier.append(node(left = left,
                                         right = right,
                                         indl = left.indl, 
                                         indr = right.indr, 
                                         val = self.op([left.val, right.val])
                                        ))
                
                else: 
                    frontier.append(node(left = left,
                                         right = None,
                                         indl = left.indl, 
                                         indr = left.indr, 
                                         val = left.val
                                        ))
            
        return frontier.pop()           

    def level_order_traversal(self):
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.indl, node.indr, node.val)    
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)

    def query(self, l, r):

        # makes it so I can only support these ops
        if self.op == min:
            ans = float('inf')
        elif self.op == max:
            ans = float('-inf')
        elif self.op == sum:
            ans = 0 

        if l > r:
            return None
        if not self.root:
            return None
        if self.root.indl > l or self.root.indr < r:
            return None

        queue = [self.root]
        while queue:
            node = queue.pop(0)
            # range within query
            if node.indl >= l and node.indr <= r:
                ans = self.op([ans, node.val])
            # query within range
            elif node.indl <= l <= node.indr or node.indl <= r <= node.indr:
                queue.append(node.left)
                # if level has odd number of nodes
                if node.right:
                    queue.append(node.right)
             
        return ans
        
    def update(self, ind, val):
        
        if not self.root:
            return
        if ind > self.root.indr:
            return

        
        stack = [self.root]
        node = self.root
        l = node.indl
        r = node.indr
        while l != r:
            
            left = node.left
            right = node.right
            if left and left.indl <= ind <= left.indr:
                node = left
                l = left.indl
                r = left.indr
            elif right and right.indl <= ind <= right.indr:
                node = right
                l = right.indl
                r = right.indr
            
            stack.append(node)
        
        while stack:                
            
            node = stack.pop()
            if not node.right:
                node.val = val
            else:
                node.val = self.op([node.left.val, node.right.val])



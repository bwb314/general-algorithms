class minheap:

    def __init__(self):

        self.heap = []


    def push(self, val):

        node = len(self.heap)
        self.heap.append(val)
        # Bubble up
        while node > 0:

            parent = (node - 1) // 2
            if self.heap[parent] > val:
                self.heap[node], self.heap[parent] = self.heap[parent], self.heap[node]
                node = parent
            else:
                break

    def poppush(self, val):

        # pop
        ans = self.heap[0]
        self.heap[0] = val
        
        node = 0
        left = 1 
        right = 2
        # Bubble down
        while left or right:
            swapnode = node
            if left < len(self.heap) and self.heap[left] < self.heap[node]:
                swapnode = left
            if right < len(self.heap) and self.heap[right] < self.heap[node]:
                if self.heap[right] < self.heap[swapnode]:
                    swapnode = right    
            if swapnode == node:
                break

            self.heap[node], self.heap[swapnode] = self.heap[swapnode], self.heap[node]
            node = swapnode
            left = 2 * node + 1                
            right = 2 * node + 2

        return ans

    def popmin(self):

        # No min if no elements
        if len(self.heap) > 0:
            ans = self.heap[0]
        else:
            return None
        # Can't pop and set and if len 1
        if len(self.heap) > 1:
            self.heap[0] = self.heap.pop() 
        
        node = 0
        left = 1 
        right = 2
        # Bubble down
        while left or right:
            swapnode = node
            if left < len(self.heap) and self.heap[left] < self.heap[node]:
                swapnode = left
            if right < len(self.heap) and self.heap[right] < self.heap[node]:
                if self.heap[right] < self.heap[swapnode]:
                    swapnode = right    
            if swapnode == node:
                break

            self.heap[node], self.heap[swapnode] = self.heap[swapnode], self.heap[node]
            node = swapnode
            left = 2 * node + 1                
            right = 2 * node + 2
    
        return ans     

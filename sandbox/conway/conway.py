import numpy as np

class Life:

    def __init__(self, w, h):

        self.w = w
        self.h = h
        self.board = np.random.randint(2, size=(h,w))
       

    def print_board(self):

        for row in self.board:

            for cell in row:

                if cell:

                    print("0", end = "")

                else:

                    print(" ", end = "")

            print("\n")


    def step(self):

        new_board = np.zeros((self.h, self.w))

        for i, row in enumerate(self.board):
        
            for j, cell in enumerate(row):

                new_board[i][j] = self.alive(i,j)
        
        self.board = new_board

    def alive(self, i, j):

        
        count = 0

        for x in range(-1,2):
       
            if i == 0 and x == -1:

                continue
            
            if i == self.h - 1 and x == 1:

                continue

            for y in range(-1,2):
            
                if j == 0 and y == -1:

                    continue
                
                if j == self.w - 1 and y == 1:

                    continue
                    
                if self.board[i+x][j+y]==1 and (x,y) != (0,0):

                    count += 1

        if (count == 3) or (count == 2 and self.board[i][j] == 1):

            return 1

        else:

            return 0


    def play(self, n):

        import time
        print(self.w*'_')
        self.print_board()          
        print(self.w*'_')

        for _ in range(n):

            time.sleep(0.6)
            self.step()
            self.print_board()          
            print(self.w*'_')





game = Life(180,26)

game.play(5000) 
        

        

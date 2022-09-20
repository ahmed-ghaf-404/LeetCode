# submission: https://leetcode.com/submissions/detail/804086022/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def getNeighbors(x,y):
            neighbors = [(i,j) for i in range(x-1, x+2) for j in range(y-1, y+2) if (i>=0 and i<len(board) and j>=0 and j<len(board[0]) and not(x==i and y==j))]
            return neighbors
        
        def getLivingNeighbors(x,y):            
            neighbors = getNeighbors(x,y)
            living_neighbors = []
            for i, j in neighbors:
                if board[i][j]==1:
                    living_neighbors.append((i,j))
            return living_neighbors
        
        def getNextGenState():
            # returns what to set to 0 and what to set to 1
            dies = []
            lives = []
            
            for i in range(len(board)):
                for j in range(len(board[0])):
                    living_neighbors = getLivingNeighbors(i,j)
                    # is alive
                    if board[i][j] == 1:
                        # case 1: less than 2 neighbors
                        # case 3: more than 3 neighbors
                        if len(living_neighbors) < 2 or len(living_neighbors) > 3:
                            dies.append((i,j))
                        # case 2: 2 or 3 neighbors
                        # do nothing. They remain alive

                    #is dead
                    elif len(living_neighbors) ==3:
                        # case 1: exactly 3 neighbors
                        lives.append((i,j))
            return lives, dies
        lives, dies = getNextGenState()
        # lives
        for i, j in lives:
            board[i][j] = 1
        for i,j in dies:
            board[i][j] = 0
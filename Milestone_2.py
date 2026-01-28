#Reference: https://www.geeksforgeeks.org/dsa/minimum-steps-reach-target-knight/
#           https://www.geeksforgeeks.org/dsa/breadth-first-search-or-bfs-for-a-graph/

from collections import deque

class Chess(object):
    
    def __init__(self, size_x, size_y, start_x, start_y, piece):
        self.size_x = size_x
        self.size_y = size_y
        self.start_x = start_x
        self.start_y = start_y
        self.piece = piece
        
    def valid_moves(self, x, y):
        
        moves = []
        
        #assume pawn only moves one step forward a time
        #disregard the rule when the pawn can move two steps ahead at its first move.
        #disregard pawn promotion in this milestone
        if self.piece == "pawn":
            
            if 0 <= y + 1 < self.size_y:
                
                moves.append((x, y + 1))          
        
        elif self.piece == "knight":
            
            directions = [
                (2, 1), 
                (1, 2), 
                (-1, 2), 
                (-2, 1),
                (-2, -1), 
                (-1, -2), 
                (1, -2), 
                (2, -1)
            ]

            for dx, dy in directions:
                
                nx = x + dx
                ny = y + dy
                
                if 0 <= nx < self.size_x and 0 <= ny < self.size_y:
                    moves.append((nx,ny))           
            
        elif self.piece == "bishop":

            directions = [
                (1, 1), #up-right
                (-1, 1), #up-left
                (-1, -1), #down-right
                (1, -1) #down-left
            ]
            
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                
                while 0 <= nx < self.size_x and 0 <= ny < self.size_y:
                    moves.append((nx, ny))
                    nx += dx
                    ny += dy           

        elif self.piece == "rook":
            
            directions = [
                (1, 0), #right
                (0, 1), #up
                (-1, 0), #left
                (0, -1) #down 
            ]
            
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                
                while 0 <= nx < self.size_x and 0 <= ny < self.size_y:
                    moves.append((nx, ny))
                    nx += dx
                    ny += dy

        elif self.piece == "queen":
            
            directions = [
                (1, 1), #up-right
                (1, 0), #right
                (-1, -1), #down-right
                (0, -1), #down
                (1, -1), #down-left
                (-1, 0), #left
                (-1, 1), #up-left
                (0, 1), #up
                 
            ]
            
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                
                while 0 <= nx < self.size_x and 0 <= ny < self.size_y:
                    moves.append((nx, ny))
                    nx += dx
                    ny += dy                  
            
        elif self.piece == "king":
            
            directions = [
                (1, 1), #up-right
                (1, 0), #right
                (-1, -1), #down-right
                (0, -1), #down
                (1, -1), #down-left
                (-1, 0), #left
                (-1, 1), #up-left
                (0, 1), #up 
            ]
            
            for dx, dy in directions:
                
                nx = x + dx
                ny = y + dy
                
                if 0 <= nx < self.size_x and 0 <= ny < self.size_y:
                    moves.append((nx,ny))
          
        return moves  
                 
    def BFS_chess_board(self):
        
        #make a 2d array that represents the chess board
        #make all the squares -1 to mark it as unvisited
        board = [[-1 for i in range(self.size_x)] for i in range(self.size_y)]
        
        queue = []
        
        start = (self.start_x, self.start_y)
        queue.append((start))
        board[self.start_y][self.start_x] = 0
        
        while queue:
            
            x, y = queue.pop(0)
            moves = self.valid_moves(x,y)
            
            for nx, ny in moves:
                    
                if board[ny][nx] == -1:
                    board[ny][nx] = board[y][x] + 1
                    queue.append((nx, ny))
                
        return board
        
    def print_board(self, board):
        
        #code to print the board nicely.
        for y in reversed(range(self.size_y)):
            for x in range(self.size_x):
                print(f"{board[y][x]:2d} ", end="")
            print()
        
if __name__ == "__main__":
    
    size_x = int(input("Enter horizontal size of the chess board: ").strip())
    size_y = int(input("Enter vertical size of the chess board: ").strip())
    start_x = int(input("Enter the x-coordinate of the starting position: ").strip())
    start_y = int(input("Enter the y-coordinate of the starting position: ").strip())
    piece = str(input("Enter the piece name: ").strip())

    n = int(input("Enter the number of blocking pieces: ").strip())
    
    for i in range(n):
        input("Enter the coordinates of the blocking pieces: ").strip()

    c = Chess(size_x, size_y, start_x, start_y, piece)
    b = c.BFS_chess_board()
    c.print_board(b)
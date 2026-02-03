#Reference: https://www.geeksforgeeks.org/dsa/minimum-steps-reach-target-knight/
#           https://www.geeksforgeeks.org/dsa/breadth-first-search-or-bfs-for-a-graph/

from collections import deque

class Chess(object):
    
    def __init__(self, size_x, size_y, start_x, start_y, piece, blocks):
        self.size_x = size_x
        self.size_y = size_y
        self.start_x = start_x
        self.start_y = start_y
        self.piece = piece
        self.blocks = blocks
        
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
                    
                    if (nx, ny) in self.blocks:
                        break
                    
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
                    
                    if (nx, ny) in self.blocks:
                        break
                    
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
                    
                    if (nx, ny) in self.blocks:
                        break
                    
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
                    
                if (board[ny][nx] == -1) and ((nx, ny) not in self.blocks):
                    board[ny][nx] = board[y][x] + 1
                    queue.append((nx, ny))
                
        return board
        
    def print_board(self, board):
        
        #code to print the board nicely.
        for y in reversed(range(self.size_y)):
            for x in range(self.size_x):
                if (x, y) in self.blocks:
                    print(f"{'X':>2} ", end="")
                else:
                    print(f"{board[y][x]:2d} ", end="")
            print()
        
if __name__ == "__main__":
    
    # Input horizontal size
    while True:
        try:
            size_x = int(input("Enter horizontal size of the chess board: ").strip())
            if size_x <= 0:
                print("Size must be a positive integer.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    # Input vertical size
    while True:
        try:
            size_y = int(input("Enter vertical size of the chess board: ").strip())
            if size_y <= 0:
                print("Size must be a positive integer.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    # Input starting x-coordinate
    while True:
        try:
            start_x = int(input("Enter the x-coordinate of the starting position: ").strip())
            if not (0 <= start_x < size_x):
                print(f"x-coordinate must be between 0 and {size_x - 1}.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    # Input starting y-coordinate
    while True:
        try:
            start_y = int(input("Enter the y-coordinate of the starting position: ").strip())
            if not (0 <= start_y < size_y):
                print(f"y-coordinate must be between 0 and {size_y - 1}.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    # Input piece
    valid_pieces = {"pawn", "knight", "bishop", "rook", "queen", "king"}
    while True:
        piece = input("Enter the piece name: ").strip().lower()
        if piece in valid_pieces:
            break
        print(f"Invalid piece. Choose from: {', '.join(valid_pieces)}")

    # Number of blocking pieces
    while True:
        try:
            n = int(input("Enter the number of blocking pieces: ").strip())
            if n <= 0:
                print("Number of blocking pieces must be a positive integer.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")
    
    # Added a set to check for duplicate blocking pieces.
    blocks_error_check = set()
    blocks = []
    
    for i in range(n):

        while True:
            try:
                pc_x = int(input(f"Enter the x-coordinate of blocking piece {i + 1}: ").strip())
                if not (0 <= pc_x < size_x):
                    print(f"x-coordinate must be between 0 and {size_x - 1}.")
                    continue

                pc_y = int(input(f"Enter the y-coordinate of blocking piece {i + 1}: ").strip())
                if not (0 <= pc_y < size_y):
                    print(f"y-coordinate must be between 0 and {size_y - 1}.")
                    continue

                # cannot be same as starting position
                if (pc_x, pc_y) == (start_x, start_y):
                    print("Blocking piece cannot be placed on the starting position.")
                    continue

                # cannot be repeated
                if (pc_x, pc_y) in blocks:
                    print("This blocking piece already exists. Please enter a different position.")
                    continue

                # valid blocking piece
                blocks.append((pc_x, pc_y))
                blocks_error_check.add((pc_x, pc_y))
                break

            except ValueError:
                print("Please enter valid integers.")        

        
    c = Chess(size_x, size_y, start_x, start_y, piece, blocks)
    b = c.BFS_chess_board()
    c.print_board(b)
    
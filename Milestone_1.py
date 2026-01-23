#Reference: https://www.geeksforgeeks.org/dsa/minimum-steps-reach-target-knight/

from collections import deque

class Chess(object):
    
    def __init__(self, size_x, size_y, start_x, start_y, piece):
        self.size_x = size_x
        self.size_y = size_y
        self.start_x = start_x
        self.start_y = start_y
        self.piece = piece 
        
    def valid_moves(self):
        
        moves = []
        
        #assume pawn only moves one step forward a time
        #disregard the rule when the pawn can move two steps ahead at its first move.
        #disregard pawn promotion in this milestone
        if self.piece == "pawn":
            
            moves.append((self.start_x, self.start_y + 1))
            
            
        
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
                
                x = self.start_x + dx
                y = self.start_y + dy
                
                if 0 <= x < self.size_x and 0 <= y < self.size_y:
                    moves.append((x,y))
            
            
            
        elif self.piece == "bishop":

            directions = [
                (1, 1), #up-right
                (-1, 1), #up-left
                (-1, -1), #down-right
                (1, -1) #down-left
            ]
            
            for dx, dy in directions:
                x = self.start_x + dx
                y = self.start_y + dy
                
                while 0 <= x < self.size_x and 0 <= y < self.size_y:
                    moves.append((x, y))
                    x += dx
                    y += dy
            
            

        elif self.piece == "rook":
            
            directions = [
                (1, 0), #right
                (0, 1), #up
                (-1, 0), #left
                (0, -1) #down 
            ]
            
            for dx, dy in directions:
                x = self.start_x + dx
                y = self.start_y + dy
                
                while 0 <= x < self.size_x and 0 <= y < self.size_y:
                    moves.append((x, y))
                    x += dx
                    y += dy

    

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
                x = self.start_x + dx
                y = self.start_y + dy
                
                while 0 <= x < self.size_x and 0 <= y < self.size_y:
                    moves.append((x, y))
                    x += dx
                    y += dy
            
                       
            
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
                
                x = self.start_x + dx
                y = self.start_y + dy
                
                if 0 <= x < self.size_x and 0 <= y < self.size_y:
                    moves.append((x,y))
          
        return moves  
                 


    def BFS_min_moves_board(self):
        # distance[y][x] = minimum moves to reach (x, y)
        distance = [
            [-1 for _ in range(self.size_x)]
            for _ in range(self.size_y)
        ]

        # BFS queue
        queue = deque()

        # start position
        start = (self.start_x, self.start_y)
        queue.append(start)
        distance[self.start_y][self.start_x] = 0

        while queue:
            x, y = queue.popleft()

            # generate moves FROM (x, y)
            self.start_x, self.start_y = x, y
            moves = self.valid_moves()

            for nx, ny in moves:

                # 1. Make sure the square is inside the board
                if 0 <= nx < self.size_x and 0 <= ny < self.size_y:

                    # 2. Check if we haven't visited it yet
                    if distance[ny][nx] == -1:
                        distance[ny][nx] = distance[y][x] + 1
                        queue.append((nx, ny))


        return distance

    def print_board(self, distance):
        for y in reversed(range(self.size_y)):
            for x in range(self.size_x):
                if distance[y][x] == -1:
                    print(" . ", end="")
                else:
                    print(f"{distance[y][x]:2d} ", end="")
            print()

    
    def reset_board(self):
        
        return 0 
    
if __name__ == "__main__":
    
    #size_x = int(input("Enter the horizontal size of the chess board:").strip())
    #size_y = int(input("Enter the vertical size of the chess board:").strip())
    #start_x = int(input("Entrer the x_coordinate of the starting position:").strip())
    #start_y = int(input("Entrer the y_coordinate of the starting position:").strip())
    #piece = str(input("Enter the name of the piece:").strip()) 
    
    c = Chess(8, 8, 0, 0, "knight")
    
    
    c.print_board(c.BFS_min_moves_board())
    
    
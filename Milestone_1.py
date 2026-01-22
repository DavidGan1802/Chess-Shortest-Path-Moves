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
            
            print(moves)
        
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
            
            print(moves)
            
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
            
            print(moves)

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

            print(moves)

        elif self.piece == "queen":
            
            directions = [
                (1, 1), #up-right
                (1, 0), #right
                (-1, -1), #down-right
                (0, -1) #down
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
            
            print(moves)            
            
        elif self.piece == "king":
            
            directions = [
                (1, 1), #up-right
                (1, 0), #right
                (-1, -1), #down-right
                (0, -1) #down
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
            
            print(moves)     

    def BFS_shortest_path(self):

        return 0

    def print_board(self):
        
        return 0 
    
    def reset_board(self):
        
        return 0 
    
if __name__ == "__main__":
    
    #size_x = int(input("Enter the horizontal size of the chess board:").strip())
    #size_y = int(input("Enter the vertical size of the chess board:").strip())
    #start_x = int(input("Entrer the x_coordinate of the starting position:").strip())
    #start_y = int(input("Entrer the y_coordinate of the starting position:").strip())
    #piece = str(input("Enter the name of the piece:").strip()) 
    
    c = Chess(8, 8, 3, 4, "king")
    
    c.valid_moves()
    
    
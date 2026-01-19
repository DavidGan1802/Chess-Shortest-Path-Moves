#Reference: https://www.geeksforgeeks.org/dsa/minimum-steps-reach-target-knight/

class Chess(object):
    
    def __init__(self, size_x, size_y, start_x, start_y, piece):
        self.size_x = size_x
        self.size_y = size_y
        self.start_x = start_x
        self.start_y = start_y
        self.piece = piece 
        
    def is_board_valid(self):
        
        return 0 <= self.start_x < self.size_x and 0 <= self.start_y < self.size_y
    
    def valid_moves(self):
        
        #assume pawn only moves one step forward a time
        #disregard the rule when the pawn can move two steps ahead at its first move.
        #disregard pawn promotion in this milestone
        if self.piece == "pawn":
            self.x_moves = [0]
            self.y_moves = [1]
   
        elif self.piece == "knight":
            self.x_moves = [-2, -1, 1, 2, 2, 1, -1, -2]
            self.y_moves = [1, 2, 2, 1, -1, -2, -2, -1]
            
        elif self.piece == "bishop":
            self.x_moves = [0]
            self.y_moves = [1]

        elif self.piece == "rook":
            self.x_moves = [0]
            self.y_moves = [1]

        elif self.piece == "queen":
            self.x_moves = [0]
            self.y_moves = [1]
            
        elif self.piece == "king":
            self.x_moves = [0]
            self.y_moves = [1]     

    def BFS_shortest_path(self):
        
        return 0 

    def print_board(self):
        
        return 0 
    
    def reset_board(self):
        
        return 0 
    
if __name__ == "__main__":
    
    size_x = int(input("Enter the horizontal size of the chess board:").strip())
    size_y = int(input("Enter the vertical size of the chess board:").strip())
    start_x = int(input("Entrer the x_coordinate of the starting position:").strip())
    start_y = int(input("Entrer the y_coordinate of the starting position:").strip())
    piece = str(input("Enter the name of the piece:").strip()) 
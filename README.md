# My Software Project for EEE 121 (Data Structures and Algorithms for Electrical and Electronics Engineering).

Given the initial starting position of a given piece, you will be asked to determine the
minimum number of moves needed to reach any position in the tile. 

The number in the output board is the number of minimum moves it will take for the chess piece
to reach the specific position. The starting position of the piece is marked as 0 and unreachable
tiles are marked as -1.

## Milestone 1:

The inputs are s1, s2, x1, y1, piece:
- s1, s2 - horizontal size and vertical size of the board respectively.
- x1, y1 - starting position of the piece (indices start at 0).
- piece - name of the piece (pawn, knight, bishop, rook, queen).



## Milestone 2:

The inputs are s1, s2, x1, y1, piece
               
               n
               
               n_1_1, n_1_2
               
               n_2_1, n_2_2

- n - number of blocking pieces. Exactly n lines should follow this
- n_i_1, n_i_2 - coordinates of the ith blocking piece. There should be n of these

Output the whole board for the minimum moves it will take for the chess pieces to reach each tile.
Disregard the rule wherein the pawn gets promoted or it can move two tiles at its first move.

Credits: Marcus Joseph Reyes and Ferdinand John Briones (EEE Professors)

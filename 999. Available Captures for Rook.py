"""On an 8 x 8 chessboard, there is exactly one white rook 'R' and some number
of white bishops 'B', black pawns 'p', and empty squares '.'. When the rook
moves, it chooses one of four cardinal directions (north, east, south, or
west), then moves in that direction until it chooses to stop, reaches the edge
of the board, captures a black pawn, or is blocked by a white bishop. A rook is
considered attacking a pawn if the rook can capture the pawn on the rook's
turn. The number of available captures for the white rook is the number of
pawns that the rook is attacking. Return the number of available captures for
the white rook.

Example 1:
Input: board = [
[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],
[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],
[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation: In this example, the rook is attacking all the pawns.

Example 2:
Input: board = [
[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],
[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],
[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],
[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 0
Explanation: The bishops are blocking the rook from attacking any of the pawns.

Example 3:
Input: board = [
[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],
[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],
[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],
[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation: The rook is attacking the pawns at positions b5, d6, and f5.

Constraints:

board.length == 8
board[i].length == 8
board[i][j] is either 'R', '.', 'B', or 'p'
There is exactly one cell with board[i][j] == 'R'"""
from typing import List


class Solution:
    @staticmethod
    def num_rook_captures(board: List[List[str]]) -> int:
        rook_row_index: int = -1
        rook_index_in_row: int = -1
        for index, row in enumerate(board):
            if 'R' in row:
                rook_row_index = index
                rook_index_in_row = row.index('R')
        rook_column: List = [x[rook_index_in_row] for x in board]
        rook_row: List = board[rook_row_index]
        rook_move_variants: List = [rook_column[:rook_row_index][::-1],
                                    rook_column[rook_row_index + 1:],
                                    rook_row[:rook_index_in_row][::-1],
                                    rook_row[rook_index_in_row + 1:]]
        count_attack: int = 0
        for move in rook_move_variants:
            for cell in move:
                if cell == 'p':
                    count_attack += 1
                    break
                elif cell == 'B':
                    break
        return count_attack


assert Solution.num_rook_captures(
    [[".", ".", ".", ".", ".", ".", ".", "."],
     [".", ".", ".", "p", ".", ".", ".", "."],
     [".", ".", ".", "R", ".", ".", ".", "p"],
     [".", ".", ".", ".", ".", ".", ".", "."],
     [".", ".", ".", ".", ".", ".", ".", "."],
     [".", ".", ".", "p", ".", ".", ".", "."],
     [".", ".", ".", ".", ".", ".", ".", "."],
     [".", ".", ".", ".", ".", ".", ".", "."]]) == 3

assert Solution.num_rook_captures(
    [[".", ".", ".", ".", ".", ".", ".", "."],
     [".", "p", "p", "p", "p", "p", ".", "."],
     [".", "p", "p", "B", "p", "p", ".", "."],
     [".", "p", "B", "R", "B", "p", ".", "."],
     [".", "p", "p", "B", "p", "p", ".", "."],
     [".", "p", "p", "p", "p", "p", ".", "."],
     [".", ".", ".", ".", ".", ".", ".", "."],
     [".", ".", ".", ".", ".", ".", ".", "."]]) == 0

assert Solution.num_rook_captures(
    [[".", ".", ".", ".", ".", ".", ".", "."],
     [".", ".", ".", "p", ".", ".", ".", "."],
     [".", ".", ".", "p", ".", ".", ".", "."],
     ["p", "p", ".", "R", ".", "p", "B", "."],
     [".", ".", ".", ".", ".", ".", ".", "."],
     [".", ".", ".", "B", ".", ".", ".", "."],
     [".", ".", ".", "p", ".", ".", ".", "."],
     [".", ".", ".", ".", ".", ".", ".", "."]]) == 3

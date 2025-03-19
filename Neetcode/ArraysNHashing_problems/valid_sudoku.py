from typing import List

"""
* You are given a a 9 x 9 Sudoku board board. A Sudoku board
* is valid if the following rules are followed:

! Each row must contain the digits 1-9 without duplicates.
! Each column must contain the digits 1-9 without duplicates.
! Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
! Return true if the Sudoku board is valid, otherwise return false

?Note: A board does not need to be full or be solvable to be valid.


9 x 9 grid gathering
    for i in range(9):
        print(f"Row: {test_board[i]}")
        for j in range(9):
            print(f"Col: {test_board[j][i]}")

 3 x 3 grid gathering:
    for i in range(3):
        for j in range(3):
            print(f"{test_board[j][i]}")
"""


def isValidSudoku(board: List[List[str]]) -> bool:

    temp_dict = {}

    # let's check the rows!
    for row in board:
        for number in row:
            if number not in temp_dict and number != ".":
                temp_dict[number] = 1
            elif number != ".":
                print(f"Encountered a duplicate value")
                return False
        temp_dict = {}

    temp_dict = {}

    # let's check the columns
    for i in range(9):
        for j in range(9):
            if board[j][i] not in temp_dict and board[j][i] != ".":
                temp_dict[board[j][i]] = 1
            elif board[j][i] != ".":
                print(f"Encountered a duplicate value")
                return False
        temp_dict = {}

    temp_dict = {}

    # let's check each 3x3 sub-box
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            for i in range(3):
                for j in range(3):
                    curr = board[box_row + i][box_col + j]
                    if curr not in temp_dict and curr != ".":
                        temp_dict[curr] = 1
                    elif curr != ".":
                        print(f"Encountered a duplicate value")
                        return False
            print(temp_dict)
            temp_dict = {}

    return True


isValidSudoku(
    [
        ["1", "2", ".", ".", "3", ".", ".", ".", "."],
        ["4", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", ".", "3"],
        ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
        [".", ".", ".", "8", ".", "3", ".", ".", "5"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", ".", ".", ".", ".", ".", "2", ".", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "8"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
)

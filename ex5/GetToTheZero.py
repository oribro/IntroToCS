#############################################################
# FILE: GetToTheZero.py
# WRITER: Ori Broda, orib, 308043447
# EXERCISE : intro2cs ex5 2013-2014
# Description : This program checks if a given puzzle is
# solvable or not.
#############################################################

# The minimal starting value
START_MIN = 0
# The end of the puzzle
FINISH = 0

def is_solvable(start, board):
    """ This function calls for the recursive function in order
    to find out if the board is solvable or not.

    Args:
    -start: The starting position we wish to start checking from,
    An integer (index in a list).
    -board: The board we wish to check if solvable or not. A list.

    Returns the recursive function's value: True if solvable or
    False if unsolvable."""

    # Variable for copying the board so we can check it.
    board_replica = []
    return is_solvable_helper(start, board, board_replica)
    
def is_solvable_helper(start, board, board_replica):
    """ This recursive function finds if the puzzle can be solved.
    It checks in all directions until a dead end is reached.
    The amount of steps to move each time is defined by the value
    in each square of the puzzle - a number in board (board -> list)

    Args:
    -start: The starting position we wish to start checking from,
    An integer (index in a list).
    -board: The board we wish to check if solvable or not. A list.
    -board_replica: A copied board. Used to check if we have been
    to a position so we don't have to return to it again. A list.

    Returns True if solvable or False if unsolvable."""

    # Checking for ilegal input.
    if start < START_MIN or start >= len(board):
        return False
    # We have been to here.
    if start in board_replica:
        return False
    # Puzzle is solved.
    if board[start] == FINISH:
        return True
    # Cannot move either way.
    elif start+board[start] >= len(board) and\
    start-board[start] < START_MIN:
        return False

    # Adding the current position so we don't need to return to here.
    board_replica.append(start)

    # Moving towards the end.
    forward = is_solvable_helper(start+board[start], board, board_replica)
    # Moving towards the start.
    backward = is_solvable_helper(start-board[start], board, board_replica)
    # Solved by moving either way.
    if forward or backward:
        return True
    return False
    

            
    

    



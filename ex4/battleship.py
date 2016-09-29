#############################################################
# FILE: battleship.py
# WRITER: Ori Broda
# EXERCISE : intro2cs ex4 2013-2014
# Description : Plays the battleship game
#############################################################


def new_board(width=10,height=None):

    """creates a new board game for a Battleship game.

    Args:
    -width: a positive int - the width of the board - default value 10
    -height: a positive int - the height of the board - if not spcified
    should be as width

    return: a NEW enpty board - each inner arrays is a list of 'None's.

    n case of bad input: values are out of range returns None

    You can assume that the types of the input arguments are correct."""
    
    # Checking for ilegal input
    if (width == None) and (height == None):
        return None
    if (width != None) and (height == None):
        height = width
    if (width <= 0) or (height <= 0):
        return None
    # An empty board
    board = []
    for index1 in range(height):
        # The horizontal lines of the board
        row = []
        for index2 in range(width):
            row.append(None)
        board.append(row)
    return board        
        
def place_ship(board,ship_length,bow,ship_direction):

    """Put a new ship on the board

    put a new ship (with unique index) on the board.
    in case of successful placing edit the board according to the
    definitions in the ex description.

    Args:
    -board - battleshipe board - you can assume its legal
    -ship_length: a positive int the length of the ship
    -bow: a tuple of ints the index of the ship's bow
    -ship_direction: a tuple of ints representing the direction the ship
    is facing (dx,dy) - should be out of the 4 options(E,N,W,S):
    (1,0) -facing east, rest of ship is to west of bow,

    (0,-1) - facing north, rest of ship is to south of bow, and etc.

    return: the in2dex of the placed ship, if the placement was
    successful, and 'None' otherwise.

    In case of bad input: values are out of range returns None

    You can assume the board is legal. You can assume the other inputs
    are of the right form. You need to check that they are legal."""

    # Checking for legal bow height coordinate.
    if(bow[1] not in range(len(board)) or
        # Checking for legal bow width coordinate.
        bow[0] not in range(len(board[0])) or
        # Checking if the ship can be placed within the board's limits
        bow[1]-(ship_length-1)*ship_direction[1] not in
        range(len(board)) or
        bow[0]-(ship_length-1)*ship_direction[0] not in
        range(len(board[0]))):
        return None
    # Checking for legal direction
    if ship_direction not in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        return None
    # Checking if the designated space is occupied
    for unit_length in range(ship_length):
        if(board[bow[1] - unit_length*ship_direction[1]]
                [bow[0] - unit_length*ship_direction[0]] is not None):
            return None
    # Size stored in list as required.
    ship_length_list = [ship_length]
    # Index for the new ship
    ship_index = 1
    # Checking for existing ships to determine the new index for
    # the ship to be placed
    for column in range(len(board)):
        for row in range(len(board[0])):
            if (board[column][row] is not None and
                    ship_index < board[column][row][0]):
                ship_index = board[column][row][0] + 1
    # Placing the new ship
    for unit_length in range(ship_length):
        (board[bow[1] - unit_length*ship_direction[1]]
         [bow[0] - unit_length*ship_direction[0]]) =\
         (ship_index, unit_length, ship_length_list)
    return ship_index


def fire(board,target):
    """implement a fire in battleship game

    Calling this function will try to destroy a part in one of the
    ships on the board. In case of successful fire destroy
    the relevant part in the damaged ship by deleting it from the board.
    deal also with the case of a ship which was completely destroyed

    -board - battleship board - you can assume its legal
    -target: a tuple of ints (x,y) indices on the board
    in case of illegal target return None

    returns: a tuple (hit,ship), where hit is True/False depending if
    the the shot hit, and ship is the index of the ship which was
    completely destroyed, or 0 if no ship was completely destroyed.
    or 0 if no ship was completely destroyed.

    Return None in case of bad input

    You can assume the board is legal. You can assume the other inputs
    are of the right form. You need to check that they are legal."""


    # Looking for the target's existence.
    if (target[1] not in range(len(board)) or
        target[0] not in range(len(board[0]))):
        return None
    # Target is found.
    if board[target[1]][target[0]] is not None:
        # The ship is destroyed.
        if board[target[1]][target[0]][2] == [1]:
            destroyed_ship = board[target[1]][target[0]][0]
            board[target[1]][target[0]] = None
            return (True, destroyed_ship)
        # The designated part of the ship is destroyed, but the ship
        # didn't sink
        if board[target[1]][target[0]][2] != [1]:
            board[target[1]][target[0]][2][0] -= 1
            board[target[1]][target[0]] = None
            return (True, 0)
    return (False, 0)
   

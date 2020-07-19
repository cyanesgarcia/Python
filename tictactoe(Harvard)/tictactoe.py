import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    numberX = board[0].count('X') + board[1].count('X') + board[2].count('X')
    numberO = board[0].count('O') + board[1].count('O') + board[2].count('O')
    if (len(set(board[0])) == len(set(board[1])) == len(set(board[2])) == 1 and board[0][0] == None and board[1][0] == None and board[2][0] == None):
        return 'X'
    elif(numberX == numberO):
        return 'X'
    else:
        return 'O'        
    raise NotImplementedError



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    tarray= []
    for i in range(3):
        for j in range(3):
            if(board[i][j] is None):
                tarray.append((i,j))
    return tarray 
    raise NotImplementedError



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    bcopy = copy.deepcopy(board)
    if bcopy[action[0]][action[1]] is not None:
        raise NameError('Not valid action')
    else:
        bcopy[action[0]][action[1]] = player(bcopy)
        return bcopy
    raise NotImplementedError
   


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    import numpy as np
    a=np.array(board)
    if (len(set(board[0])) == 1 and not (board[0][0] == None)):
        return board[0][0]
    elif (len(set(board[1])) == 1 and not (board[1][0] == None)):
        return board[1][0]
    elif (len(set(board[2])) == 1 and not (board[2][0] == None)):
        return board[2][0]
    elif (len(set(a[:, 0])) == 1 and not (board[0][0] == None)):
        return board[0][0]
    elif (len(set(a[:, 1])) == 1 and not (board[0][1] == None)):
        return board[0][1]
    elif (len(set(a[:, 2])) == 1 and not (board[0][2] == None)):
        return board[0][2]
    elif (board[0][0] == board[1][1] == board[2][2] and not (board[0][0] == None)):
        return board[0][0]
    elif (board[0][2] == board[1][1] == board[2][0] and not (board[0][2] == None)):
        return board[0][2]
    else:
        return None    
    raise NotImplementedError



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if((None not in board[0] and None not in board[1] and None not in board[2]) or winner(board)== 'X' or winner(board)=='O'):
        return True
    else:
        return False
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if(winner(board)== 'X'):
        return 1
    elif(winner(board)=='O'):
        return -1
    else:
        return 0
    raise NotImplementedError

def minimax(board):
    if player(board) == X:
        v = -999999999999999999
        for action in actions(board):
            k = min_value(result(board, action))
            if k > v:
                v = k
                bestaction = action
    else:
        v = 999999999999999999
        for action in actions(board):
            k = max_value(result(board, action))
            if k < v:
                v = k
                bestaction = action
    return bestaction

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -999999999999999999
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = 999999999999999999
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v    #FIXED

"""
Tic Tac Toe Player
"""

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
    if not terminal(board):
    # 1. Conte a quantidade de símbolos no tabuleiro
        qt = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] != EMPTY:
                    qt += 1

        # 2. Retorne X se a quantidade for par. Caso contrário, retorne O
        if qt % 2 == 0: 
            return X
        else: 
            return O
    
    
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    # 1. Inicialize um conjunto vazio
    conjunto = set()

    # 2. Itere sobre o tabuleiro procurando espaços vazios. Ao encontrar, adicione suas coodenadas no conjunto
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                tupla = (i, j)
                conjunto.add(tupla)

    return conjunto


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action 

    index_in_bounds = (0 <= i <= 2) and (0 <= j <= 2)
    if board[i][j] != EMPTY or not index_in_bounds:
        raise Exception('invalid move')

    b = copy.deepcopy(board)
    b[i][j] = player(board)
    
    return b
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    dp = board[0][0] == board[1][1] == board[2][2]
    ds = board[2][0] == board[1][1] == board[0][2]
    
    l0 = board[0][0] == board[0][1] == board[0][2]
    l1 = board[1][0] == board[1][1] == board[1][2]
    l2 = board[2][0] == board[2][1] == board[2][2]

    c0 = board[0][0] == board[1][0] == board[2][0]
    c1 = board[0][1] == board[1][1] == board[2][1]
    c2 = board[0][2] == board[1][2] == board[2][2] 
    
    caso_1 = (dp or l0 or c0) and board[0][0] != EMPTY
    caso_2 = (ds or l1 or c1) and board[1][1] != EMPTY
    caso_3 = (l2 or c2)       and board[2][2] != EMPTY
    
    winner = None
    if caso_1: 
        winner = board[0][0]
    elif caso_2: 
        winner = board[1][1]
    elif caso_3:
        winner = board[2][2]

    return winner


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    has_winner = winner(board) != None
    is_tie = len(actions(board)) == 0

    return has_winner or is_tie 


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    jogador = player(board)
    acoes = actions(board)

    aux = {}
    
    if jogador == X:
        for action in acoes:
            newBoard = result(board, action)
            v = min_value(newBoard)
            aux[v] = action
    
        key = max(list(aux.keys()))
        return aux[key]

    elif jogador == O:
        for action in acoes:
            newBoard = result(board, action)
            v = max_value(newBoard)
            aux[v] = action
        
        key = min(list(aux.keys())) 
        return aux[key]


def max_value(board):
    if terminal(board):
        return utility(board)       

    v = -10     #Um número arbitrariamente pequeno
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v
    

def min_value(board):
    if terminal(board):
        return utility(board)       

    v = 10     #Um número arbitrariamente grande
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

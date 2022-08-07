import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    movX = 0
    movO = 0
    for i in range(3):
        movX += board[i].count(X)
        movO += board[i].count(O)
    if movX > movO:
        return O
    return X


def actions(board):
    moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                moves.add((i, j))

    return moves


def result(board, action):
    r = action[0]
    c = action[1]
    possibility = copy.deepcopy(board)
    if player(board) == X:
        possibility[r][c] = X
    else:
        possibility[r][c] = O

    return possibility


def winner(board):
    temp = copy.deepcopy(board)
    for i in range(3):
        if temp[i].count(X) == 3: return X
        if temp[i].count(O) == 3: return O

    temp = list(map(list, zip(*board)))

    for i in range(3):
        if temp[i].count(X) == 3: return X
        if temp[i].count(O) == 3: return O

    d1 = []
    d2 = []
    for i in range(3):
        d1.append(temp[i][i])
        d2.append(temp[i][2-i])

    if d1.count(X) == 3 or d2.count(X) == 3: return X
    if d1.count(O) == 3 or d2.count(O) == 3: return O

    return None


def terminal(board):
    for i in range(3):
        if board[i].count(EMPTY) > 0:
            return winner(board) != None

    return True


def utility(board):
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1

    return 0


def minimax(board,max_p):
    if terminal(board):
        return None, utility(board)


    moves = actions(board)
    optMove = (0,0)
    if max_p:
        optVal = -math.inf
        for move in moves:
            val = minimax(result(board,move),False)[1]
            if val > optVal:
                optMove = move
                optVal = val
        return optMove,optVal
    else:
        optVal = math.inf
        for move in moves:
            val = minimax(result(board, move),True)[1]
            if val < optVal:
                optMove = move
                optVal = val
    return optMove,optVal
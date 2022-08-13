#file to get win/tie/lose stats of A.I

import tictactoe as ttt
import itertools

X = "X"
O = "O"
E = None

wins = 0
loses = 0
ties = 0

allMoves = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
movePerms = itertools.permutations(allMoves,4)


#def prefixCheck(moves,prefixList):
#    return False

for moves in movePerms:
    turnC = 0
    user = O
    board = ttt.initial_state()
    ai_turn = False
    print(moves)
    print()

    while True:
        game_over = ttt.terminal(board)
        player = ttt.player(board)

        if game_over:
            winner = ttt.winner(board)
            if winner is None:
                ties+=1
            elif winner is X:
                wins+=1
            else:
                loses+=1
            break

        if user != player and not game_over:
            if ai_turn:
                move = ttt.minimax(board,user == ttt.O)[0]
                board = ttt.result(board, move)
                ai_turn = False
            else:
                ai_turn = True

        if user is player and not game_over:
            if board[moves[turnC][0]][moves[turnC][1]] != E:
                break
            board = ttt.result(board,moves[turnC])
            turnC+=1
            for i in range(3):
                print(board[i])
            print()
            print("Wins: {0} Loses: {1} Ties: {2}".format(wins,loses,ties))
            print()

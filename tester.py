import tictactoe as ttt
X = "X"
O = "O"
E = None
game = [
    [X,O,O],
    [O,X,O],
    [X,X,O]
]
print(ttt.winner(game))
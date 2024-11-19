from pieces import *
from tools import Position

def GetFenPieces(character, x, y):
    FenPieces = {
    "K": King(Position(x, y), 0),
    "Q": Queen(Position(x, y), 0),
    "B": Bishop(Position(x, y), 0),
    "N": Knight(Position(x, y), 0),
    "R": Rook(Position(x, y), 0),
    "P": Pawn(Position(x, y), 0),

    "k": King(Position(x, y), 1),
    "q": Queen(Position(x, y), 1),
    "b": Bishop(Position(x, y), 1),
    "n": Knight(Position(x, y), 1),
    "r": Rook(Position(x, y), 1),
    "p": Pawn(Position(x, y), 1),
    }

    if character in FenPieces:
        return FenPieces[character]
    else:
        return None

# The fen notation function return a grid of the formated Position
def FEN(positionstring):
    boardSize = 8
    boardGrid = [[None for _ in range(boardSize)] for _ in range(boardSize)]
    row = 0
    col = 0

    positionstring = positionstring.split()[0]

    for character in positionstring:
        if character.isdigit():
            col += int(character)
        elif character == '/':
            row += 1
            col = 0
        else:
            if row < boardSize and col < boardSize:
                piece = GetFenPieces(character, row, col)  
                boardGrid[row][col] = piece
            col += 1  

    return boardGrid




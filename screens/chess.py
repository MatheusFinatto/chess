from board import Board
from Minimax.chessAI import Minimax

AI_DEPTH = 3

class Chess:
    def __init__(self):
        self.board = Board()
        self.gameOver = False
        # Minimax(depth, chess_board, activate_alpha_beta_pruning = Default(true), UsePointMaps = Default(true))
        self.ComputerAI = Minimax(AI_DEPTH, self.board, True, True)

    def set_fen(self, fen):
        self.board.set_fen(fen) 

    def IsGameOver(self):
        if self.board.winner != None:
            self.gameOver = True

    def vsComputer(self):
            return self.ComputerMoves()


    def ComputerMoves(self):
            piece, best_move = self.ComputerAI.Start(0)
            self.board.Move(piece, best_move)
            if self.board.pieceToPromote != None:
                self.board.PromotePawn(self.board.pieceToPromote, 0)
            return piece, best_move
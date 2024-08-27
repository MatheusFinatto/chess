from flask import Flask, request, jsonify
from flask_cors import CORS
import chess
from helpers.evaluations import *

app = Flask(__name__)
CORS(app)

def piece_square_value(piece, square):
    """Get the value of a piece on a given square based on piece-square tables."""
    if piece.piece_type == chess.PAWN:
        table = pawn_eval_white if piece.color == chess.WHITE else pawn_eval_black
    elif piece.piece_type == chess.KNIGHT:
        table = knight_eval
    elif piece.piece_type == chess.BISHOP:
        table = bishop_eval_white if piece.color == chess.WHITE else bishop_eval_black
    elif piece.piece_type == chess.ROOK:
        table = rook_eval_white if piece.color == chess.WHITE else rook_eval_black
    elif piece.piece_type == chess.QUEEN:
        table = eval_queen
    elif piece.piece_type == chess.KING:
        table = king_eval_white if piece.color == chess.WHITE else king_eval_black
    else:
        return 0
    
    row = chess.square_rank(square)
    col = chess.square_file(square)
    
    return table[row][col]

def evaluate_board(board):    
    if board.is_checkmate():
        return -9999 if board.turn else 9999
    if board.is_stalemate() or board.is_insufficient_material() or board.is_seventyfive_moves() or board.is_fivefold_repetition():
        return 0

    score = 0
    for square, piece in board.piece_map().items():
        score += piece_value(piece)
        score += piece_square_value(piece, square)
    
    return score


def piece_value(piece):
    values = {
        chess.PAWN: 100,
        chess.KNIGHT: 320,
        chess.BISHOP: 330,
        chess.ROOK: 500,
        chess.QUEEN: 900,
        chess.KING: 20000  
    }

    return values[piece.piece_type] if piece.color == chess.WHITE else -values[piece.piece_type]

def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board), None

    best_move = None
    if maximizing_player:
        max_eval = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            eval, _ = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval, _ = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

def get_best_move(fen):
    board = chess.Board(fen)
    _, best_move = minimax(board, depth=3, alpha=float('-inf'), beta=float('inf'), maximizing_player=board.turn)
    return board.san(best_move)

@app.route('/move', methods=['POST'])
def get_move():
    data = request.get_json()
    fen = data.get('fen', '')
    move = get_best_move(fen)
    return jsonify({'move': move})

if __name__ == '__main__':
    app.run(debug=True)

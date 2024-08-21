from flask import Flask, request, jsonify
from flask_cors import CORS
import chess
import chess.engine

app = Flask(__name__)
CORS(app)

def evaluate_board(board):
    # A simplified evaluation function
    if board.is_checkmate():
        if board.turn:
            return -9999  # Black wins
        else:
            return 9999  # White wins
    elif board.is_stalemate() or board.is_insufficient_material():
        return 0  # Draw
    else:
        material = sum([
            len(board.pieces(piece_type, chess.WHITE)) - len(board.pieces(piece_type, chess.BLACK))
            for piece_type in chess.PIECE_TYPES
        ])
        return material

def minimax(board, depth, alpha, beta, is_maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)
    
    legal_moves = list(board.legal_moves)
    if is_maximizing_player:
        max_eval = -float('inf')
        for move in legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def get_best_move(fen, depth=3):
    board = chess.Board(fen)
    best_move = None
    best_value = -float('inf') if board.turn else float('inf')
    
    for move in board.legal_moves:
        board.push(move)
        board_value = minimax(board, depth - 1, -float('inf'), float('inf'), not board.turn)
        board.pop()

        if (board.turn and board_value > best_value) or (not board.turn and board_value < best_value):
            best_value = board_value
            best_move = move
    
    return best_move.uci() if best_move else None

@app.route('/move', methods=['POST'])
def get_move():
    data = request.get_json()
    fen = data.get('fen', '')
    depth = data.get('depth', 3)
    move = get_best_move(fen, depth)
    return jsonify({'move': move})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
from flask_cors import CORS
import chess
import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from common import minimax


app = Flask(__name__)
CORS(app)

def find_best_move(fen):
    board = chess.Board(fen)
    _, best_move = minimax(board, depth=3, alpha=float('-inf'), beta=float('inf'), maximizing_player=board.turn)
    return board.san(best_move)

@app.route('/move', methods=['POST'])
def get_move():
    data = request.get_json()
    fen = data.get('fen', '')
    move = find_best_move(fen)
    return jsonify({'move': move})

if __name__ == '__main__':
    app.run(debug=True)

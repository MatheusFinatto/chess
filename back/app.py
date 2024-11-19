from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os
import chess

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

depth = 3

app = Flask(__name__)
CORS(app)

from screens.chess import Chess



def find_best_move(fen):
    engine = Chess()
    engine.set_fen(fen)
    board = chess.Board(fen)
    _, best_move = engine.vsComputer()
    print("best",best_move)
    if best_move is not None:
        return board.san(best_move)


@app.route('/move', methods=['POST'])
def get_move():
    data = request.get_json()
    fen = data.get('fen', '')
    move = find_best_move(fen)
    return jsonify({'move': move})

if __name__ == '__main__':
    app.run(debug=True)

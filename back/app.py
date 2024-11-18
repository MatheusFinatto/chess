from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

depth = 3

app = Flask(__name__)
CORS(app)

from Minimax.chessAI import Minimax
from board import Board


def find_best_move(fen):
    ComputerAI = Minimax(3, Board, True, True)
    _, best_move = ComputerAI.Start(0)
    return Board.san(best_move)


@app.route('/move', methods=['POST'])
def get_move():
    data = request.get_json()
    fen = data.get('fen', '')
    move = find_best_move(fen)
    return jsonify({'move': move})

if __name__ == '__main__':
    app.run(debug=True)

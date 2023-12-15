from flask import Flask, request, jsonify
from flask_cors import CORS
import chess
import random

app = Flask(__name__)
CORS(app)

def get_random_move(fen):
    board = chess.Board(fen)
    legal_moves_lst = [
        board.san(move)
        for move in board.legal_moves
    ]

    random_move = random.choice(legal_moves_lst)
    return random_move

@app.route('/move', methods=['POST'])
def get_move():
    data = request.get_json()
    fen = data.get('fen', '')
    move = get_random_move(fen)
    return jsonify({'move': move})

if __name__ == '__main__':
    app.run(debug=True)

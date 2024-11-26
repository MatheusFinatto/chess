from flask import Flask, request, jsonify
from flask_cors import CORS
import chess
import chess.polyglot
import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from common import get_best_move, DEPTH


app = Flask(__name__)
CORS(app)
BOOK_PATH = "../Titans.bin"


def find_best_move(fen):
    should_use_book = True
    board = chess.Board(fen)

    if not should_use_book:
        best_move = get_best_move(DEPTH, not board.turn, board)
        return board.san(best_move)
    

    try:
        with chess.polyglot.open_reader(BOOK_PATH) as reader:
            try:
                book_move = reader.find(board)
                if book_move:
                    print(f"Move from book: {book_move.move}")
                    return board.san(book_move.move)
                else:
                    print("No book move found, falling back to Minimax.")
            except IndexError:
                print("No book entry found for this position.")
                should_use_book = False
                best_move = get_best_move(DEPTH, not board.turn, board)
                return board.san(best_move)

    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except Exception as e:
        print(f"Unexpected error loading opening book: {e}")


@app.route('/move', methods=['POST'])
def get_move():
    data = request.get_json()
    fen = data.get('fen', '')
    move = find_best_move(fen)
    return jsonify({'move': move})

if __name__ == '__main__':
    app.run(debug=True)

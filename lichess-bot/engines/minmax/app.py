#!/usr/bin/env python3


import chess
import chess.engine
import sys
import os

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.append(root_dir)

from common import minimax_root, DEPTH


def find_best_move(fen):
    board = chess.Board(fen)
    best_move = minimax_root(DEPTH, not board.turn, board)
    return board.san(best_move)

def main():
    board = chess.Board()

    while True:
        command = input().strip()

        if command == "quit":
            break

        elif command == "uci":
            print("uciok")

        elif command == "isready":
            print("readyok")

        elif command.startswith("position"):
            parts = command.split(" ")
            if "startpos" in parts:
                board.set_fen(chess.STARTING_FEN)
                if "moves" in parts:
                    moves_start = parts.index("moves") + 1
                    moves = parts[moves_start:]
                    for move in moves:
                        board.push_uci(move)
            elif "fen" in parts:
                fen_index = parts.index("fen") + 1
                fen = " ".join(parts[fen_index:fen_index + 6])
                board.set_fen(fen)
        elif command.startswith("go"):
            best_move = find_best_move(board, depth=DEPTH)
            print(f"bestmove {best_move}")
        else:
            pass

if __name__ == "__main__":
    main()

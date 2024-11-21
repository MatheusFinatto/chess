import chess

DEPTH = 4

#evaluation tables
def reverse_array(array):
    return array[::-1]

pawn_eval_white = [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0],
    [1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0],
    [0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5],
    [0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0],
    [0.5, -0.5, -1.0, 0.0, 0.0, -1.0, -0.5, 0.5],
    [0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
]

knight_eval_white = [
    [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
    [-4.0, -2.0, 0.0, 0.0, 0.0, 0.0, -2.0, -4.0],
    [-3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0],
    [-3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.5, -3.0],
    [-3.0, 0.0, 1.5, 2.0, 2.0, 1.5, 0.0, -3.0],
    [-3.0, 0.5, 1.0, 1.5, 1.5, 1.0, 0.5, -3.0],
    [-4.0, -2.0, 0.0, 0.5, 0.5, 0.0, -2.0, -4.0],
    [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
]

bishop_eval_white = [
    [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
    [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0],
    [-1.0, 0.0, 0.5, 1.0, 1.0, 0.5, 0.0, -1.0],
    [-1.0, 0.5, 0.5, 1.0, 1.0, 0.5, 0.5, -1.0],
    [-1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.0],
    [-1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0],
    [-1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, -1.0],
    [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
]

rook_eval_white = [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5],
    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
    [0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0],
]

queen_eval_white = [
    [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
    [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0],
    [-1.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0],
    [-0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5],
    [0.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5],
    [-1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0],
    [-1.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, -1.0],
    [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
]

king_eval_white = [
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
    [-1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
    [2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0],
    [2.0, 3.0, 1.0, 0.0, 0.0, 1.0, 3.0, 2.0],
]

pawn_eval_black = reverse_array(pawn_eval_white)
bishop_eval_black = reverse_array(bishop_eval_white)
knight_eval_black = reverse_array(knight_eval_white)
rook_eval_black = reverse_array(rook_eval_white)
queen_eval_black = reverse_array(queen_eval_white)
king_eval_black = reverse_array(king_eval_white)



###################################################################################################################



def evaluate_piece(piece, x, y):
    if piece is None:
        return 0

    def get_absolute_value(piece, is_white, x, y):
        # Check piece type and return the evaluation based on the piece type and position
        if piece.piece_type == chess.PAWN:
            return 10 + (pawn_eval_white[y][x] if is_white else pawn_eval_black[y][x])
        elif piece.piece_type == chess.ROOK:
            return 50 + (rook_eval_white[y][x] if is_white else rook_eval_black[y][x])
        elif piece.piece_type == chess.KNIGHT:
            return 30 + (knight_eval_white[x][y] if is_white else knight_eval_black[x][y])
        elif piece.piece_type == chess.BISHOP:
            return 30 + (bishop_eval_white[y][x] if is_white else bishop_eval_black[y][x])
        elif piece.piece_type == chess.QUEEN:
            return 90 + (queen_eval_white[y][x] if is_white else queen_eval_black[y][x])
        elif piece.piece_type == chess.KING:
            return 900 + (king_eval_white[y][x] if is_white else king_eval_black[y][x])
        else:
            raise ValueError(f"Unknown piece type: {piece.piece_type}")

    # Get the absolute value of the piece
    absolute_value = get_absolute_value(piece, piece.color == chess.WHITE, x, y)
    
    # Return positive or negative value based on the piece's color
    return absolute_value if piece.color == chess.WHITE else -absolute_value



def evaluate_board(board):
    if board.is_checkmate():
        return 10000 if board.turn == False else -10000
    total_evaluation = 0
    for i in range(8):
        for j in range(8):
            piece = board.piece_at(i * 8 + j)
            if piece:
                total_evaluation += evaluate_piece(piece, i, j)
    return total_evaluation


def minimax_root(depth, is_maximizing_player, board):
    best_value = -float('inf') if is_maximizing_player else float('inf')
    best_move_found = None

    for move in board.legal_moves:
        board.push(move)
        value = minimax(depth - 1, -float('inf'), float('inf'), not is_maximizing_player, board)
        board.pop()

        if is_maximizing_player and value > best_value:
            best_value = value
            best_move_found = move
        elif not is_maximizing_player and value < best_value:
            best_value = value
            best_move_found = move

    return best_move_found



def minimax(depth, alpha, beta, is_maximizing_player, board):
    if depth == 0:
        return -evaluate_board(board)

    if is_maximizing_player:
        best_move = -9999
        for move in board.legal_moves:
            board.push(move)
            best_move = max(best_move, minimax(depth - 1, alpha, beta, not is_maximizing_player, board))
            board.pop()
            alpha = max(alpha, best_move)
            if beta <= alpha:
                return best_move
        return best_move
    else:
        best_move = 9999
        for move in board.legal_moves:
            board.push(move)
            best_move = min(best_move, minimax(depth - 1, alpha, beta, not is_maximizing_player, board))
            board.pop()
            beta = min(beta, best_move)
            if beta <= alpha:
                return best_move
        return best_move


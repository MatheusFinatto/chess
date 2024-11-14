import chess
from typing import  List

DEPTH = 4

#valor de peças
piece_value = {
    chess.PAWN: 10,
    chess.KNIGHT: 30,
    chess.BISHOP: 30,
    chess.ROOK: 50,
    chess.QUEEN: 90,
    chess.KING: 2000
}

#evaluation tables
pawn_eval_white = [

     0,    0,   0,   0,   0,   0,   0,   0,
    50,   50,  50,  50,  50,  50,  50,  50,
    10,   10,  20,  30,  30,  20,  10,  10,
     5,    5,  10,  25,  25,  10,   5,   5,
     0,    0,   0,  20,  20,   0,   0,   0,
     5,   -5, -10,   0,   0, -10,  -5,   5,
     5,   10,  10, -20, -20,  10,  10,   5,
     0,    0,   0,   0,   0,   0,   0,   0
]


knight_eval_white = [

    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20,   0,   0,   0,   0, -20, -40,
    -30,   0,  10,  15,  15,  10,   0, -30,
    -30,   5,  15,  20,  20,  15,   5, -30,
    -30,   0,  15,  20,  20,  15,   0, -30,
    -30,   5,  10,  15,  15,  10,   5, -30,
    -40, -20,   0,   5,   5,   0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50
]


bishop_eval_white = [

     -20, -10, -10, -10, -10, -10, -10, -20,
     -10,   0,   0,   0,   0,   0,   0, -10,
     -10,   0,   5,  10,  10,   5,   0, -10,
     -10,   5,   5,  10,  10,   5,   5, -10,
     -10,   0,  10,  10,  10,  10,   0, -10,
     -10,  10,  10,  10,  10,  10,  10, -10,
     -10,   5,   0,   0,   0,   0,   5, -10,
     -20, -10, -10, -10, -10, -10, -10, -20
]


rook_eval_white = [

      0,   0,   0,   0,   0,   0,   0,  0,
      5,  10,  10,  10,  10,  10,  10,  5,
     -5,   0,   0,   0,   0,   0,   0, -5,
     -5,   0,   0,   0,   0,   0,   0, -5,
     -5,   0,   0,   0,   0,   0,   0, -5,
     -5,   0,   0,   0,   0,   0,   0, -5,
     -5,   0,   0,   0,   0,   0,   0, -5,
      0,   0,   0,   5,   5,   0,   0,  0
]


queen_eval_white = [

     -20, -10, -10, -5, -5, -10, -10, -20,
     -10,   0,   0,  0,  0,   0,   0, -10,
     -10,   0,   5,  5,  5,   5,   0, -10,
      -5,   0,   5,  5,  5,   5,   0,  -5,
       0,   0,   5,  5,  5,   5,   0,  -5,
     -10,   5,   5,  5,  5,   5,   0, -10,
     -10,   0,   5,  0,  0,   0,   0, -10,
     -20, -10, -10, -5, -5, -10, -10, -20
]

king_eval_white = [

     -30, -40, -40, -50, -50, -40, -40, -30,
     -30, -40, -40, -50, -50, -40, -40, -30,
     -30, -40, -40, -50, -50, -40, -40, -30,
     -30, -40, -40, -50, -50, -40, -40, -30,
     -20, -30, -30, -40, -40, -30, -30, -20,
     -10, -20, -20, -20, -20, -20, -20, -10,
      20,  20,  0,    0,  0,    0,  20,  20,
      20,  30,  10,   0,  0,   10,  30,  20
]

king_eval_white_endgame = [

     -50, -40, -30, -20, -20, -30, -40, -50,
     -30, -20, -10,   0,   0, -10, -20, -30,
     -30, -10,  20,  30,  30,  20, -10, -30,
     -30, -10,  30,  40,  40,  30, -10, -30,
     -30, -10,  30,  40,  40,  30, -10, -30,
     -30, -10,  20,  30,  30,  20, -10, -30,
     -30, -30,  0,    0,   0,   0, -30, -30,
     -50, -30, -30, -30, -30, -30, -30, -50
]

pawn_eval_black = list(reversed(pawn_eval_white))

knight_eval_black = list(reversed(knight_eval_white))

bishop_eval_black = list(reversed(bishop_eval_white))

rook_eval_black = list(reversed(rook_eval_white))

queen_eval_black = list(reversed(queen_eval_white))

king_eval_black = list(reversed(king_eval_white))

king_eval_black_endgame = list(reversed(king_eval_white_endgame))


###################################################################################################################

def move_value(board: chess.Board, move: chess.Move, endgame: bool) -> float:
    if move.promotion is not None:
        return -piece_value[chess.QUEEN] + 50 if board.turn == chess.BLACK else piece_value[chess.QUEEN] + 50

    # Checa se o valor da peça aumenta ao mudar de posição
    _piece = board.piece_at(move.from_square)
    if _piece:
        _from_value = evaluate_piece(_piece, move.from_square, endgame)
        _to_value = evaluate_piece(_piece, move.to_square, endgame)
        position_change = _to_value - _from_value
    else:
        raise Exception(f"Esperado peça na posição {move.from_square}")

    # Checa se o valor da peça aumenta ao capturar outra
    capture_value = 0
    if board.is_capture(move):
        capture_value = evaluate_capture(board, move)

    # Calcula o valor do movimento com mudança de valor + valor de captura
    current_move_value = capture_value + position_change
    if board.turn == chess.BLACK:
        current_move_value = -current_move_value

    return current_move_value



def evaluate_capture(board: chess.Board, move: chess.Move) -> float:
    if board.is_en_passant(move):
        return piece_value[chess.PAWN]
    
    _to = board.piece_at(move.to_square)
    _from = board.piece_at(move.from_square)

    if _to is None or _from is None:
        raise Exception(
            f"Peças esperadas em {move.to_square} e {move.from_square}"
        )
    
    return piece_value[_to.piece_type] - piece_value[_from.piece_type]


def evaluate_piece(piece: chess.Piece, square: chess.Square, end_game: bool) -> int:
    piece_type = piece.piece_type
    mapping = []
    if piece_type == chess.PAWN:
        mapping = pawn_eval_white if piece.color == chess.WHITE else pawn_eval_black
    elif piece_type == chess.KNIGHT:
        mapping = knight_eval_white if piece.color == chess.WHITE else knight_eval_black
    elif piece_type == chess.BISHOP:
        mapping = bishop_eval_white if piece.color == chess.WHITE else bishop_eval_black
    elif piece_type == chess.ROOK:
        mapping = rook_eval_white if piece.color == chess.WHITE else rook_eval_black
    elif piece_type == chess.QUEEN:
        mapping = queen_eval_white if piece.color == chess.WHITE else queen_eval_black
    elif piece_type == chess.KING:
        if end_game:
            mapping = (
                king_eval_white_endgame if piece.color == chess.WHITE else king_eval_black_endgame
            )
        else:
            mapping = king_eval_white if piece.color == chess.WHITE else king_eval_black
    
    # Adiciona verificação para garantir que `mapping` esteja preenchido
    if not mapping:
        raise ValueError(f"Tipo de peça não suportado: {piece_type}")

    return mapping[square]



def evaluate_board(board: chess.Board) -> float:
    # (+) white, (-) black
    total = 0
    end_game = is_endgame(board)

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if not piece:
            continue

        value = piece_value[piece.piece_type] + evaluate_piece(piece, square, end_game)
        total += value if piece.color == chess.WHITE else -value

    return total


def is_endgame(board: chess.Board) -> bool:
    queens = 0
    minors = 0

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece and piece.piece_type == chess.QUEEN:
            queens += 1
        if piece and (
            piece.piece_type == chess.BISHOP or piece.piece_type == chess.KNIGHT
        ):
            minors += 1

    if queens == 0 or (queens == 2 and minors <= 1):
        return True

    return False


def get_ordered_moves(board: chess.Board) -> List[chess.Move]:
    end_game = is_endgame(board)

    def orderer(move):
        return move_value(board, move, end_game)

    in_order = sorted(
        board.legal_moves, key=orderer, reverse=(board.turn == chess.WHITE)
    )
    return list(in_order)


def minimax_root(depth: int, board: chess.Board) -> chess.Move:
    # Brancas querem maximizar o board score, pretas querem minimizar
    maximize = board.turn == chess.WHITE
    best_move = -float("inf")
    if not maximize:
        best_move = float("inf")

    moves = get_ordered_moves(board)
    best_move_found = moves[0]

    for move in moves:
        board.push(move)
        if board.can_claim_draw():
            value = 0
        else:
            value = minimax(depth - 1, board, -float("inf"), float("inf"), not maximize)
        board.pop()
        if maximize and value >= best_move:
            best_move = value
            best_move_found = move
        elif not maximize and value <= best_move:
            best_move = value
            best_move_found = move

    return best_move_found




def minimax(depth, board, alpha, beta, is_maximizing_player):
    best_move = None
    # Se alcançar profundidade zero ou fim do jogo, avalia o tabuleiro
    if depth == 0 or board.is_game_over():
        return evaluate_board(board), None

    if is_maximizing_player:
        max_eval = -float("inf")
        for move in get_ordered_moves(board):
            board.push(move)
            eval, _ = minimax(depth - 1, board, alpha, beta, False)
            board.pop()
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float("inf")
        for move in get_ordered_moves(board):
            board.push(move)
            eval, _ = minimax(depth - 1, board, alpha, beta, True)
            board.pop()
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

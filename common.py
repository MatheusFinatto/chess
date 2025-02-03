import chess

DEPTH = 2
CHESSBOARD_SIZE = 8

pawn_eval_white = [
    [ 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
    [ 5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0],
    [ 1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0],
    [ 0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5],
    [ 0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0],
    [ 0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5],
    [ 0.5,  1.0,  1.0, -2.0, -2.0,  1.0,  1.0,  0.5],
    [ 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
]

knight_eval_white = [
    [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
    [-4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0],
    [-3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0],
    [-3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0],
    [-3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0],
    [-3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0],
    [-4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0],
    [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
]

bishop_eval_white = [
    [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
    [-1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
    [-1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0],
    [-1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0],
    [-1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0],
    [-1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0],
    [-1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0],
    [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
]

rook_eval_white = [
    [ 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
    [ 0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5],
    [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [-0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ 0.0,  0.0,  0.0,  0.5,  0.5,  0.0,  0.0,  0.0],
]

queen_eval_white = [
    [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
    [-1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
    [-1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
    [-0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
    [ 0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
    [-1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
    [-1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0],
    [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
]

king_eval_white = [
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
    [-1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
    [ 2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0],
    [ 2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0],
]

def reverse_array(array):
    return array[::-1]

pawn_eval_black   =   reverse_array(pawn_eval_white)
bishop_eval_black =   reverse_array(bishop_eval_white)
knight_eval_black =   reverse_array(knight_eval_white)
rook_eval_black   =   reverse_array(rook_eval_white)
queen_eval_black  =   reverse_array(queen_eval_white)
king_eval_black   =   reverse_array(king_eval_white)

####################################################################################################################################

# Valor intrínseco da peça + valor da posição na tabela de avaliação
def evaluate_piece(piece, x, y):
    if piece is None:
        return 0

    is_white = piece.color == chess.WHITE

    def get_piece_value(piece, is_white, x, y):
        if piece.piece_type == chess.PAWN:
            return 10 + (pawn_eval_white[y][x] if is_white else pawn_eval_black[y][x])
        elif piece.piece_type == chess.ROOK:
            return 50 + (rook_eval_white[y][x] if is_white else rook_eval_black[y][x])
        elif piece.piece_type == chess.KNIGHT:
            return 30 + (knight_eval_white[x][y] if is_white else knight_eval_black[y][x])
        elif piece.piece_type == chess.BISHOP:
            return 30 + (bishop_eval_white[y][x] if is_white else bishop_eval_black[y][x])
        elif piece.piece_type == chess.QUEEN:
            return 90 + (queen_eval_white[y][x] if is_white else queen_eval_black[y][x])
        elif piece.piece_type == chess.KING:
            return 900 + (king_eval_white[y][x] if is_white else king_eval_black[y][x])
        else:
            raise ValueError(f"Unknown piece type: {piece.piece_type}")

    return get_piece_value(piece, is_white, x, y) if is_white else -get_piece_value(piece, is_white, x, y)

# Somatório dos valores das peças
def evaluate_board(board, current_depth = 0):    
    if board.is_checkmate():
        return 10000 - (DEPTH - current_depth) if not board.turn else -10000 + (DEPTH - current_depth)

    elif board.is_stalemate() or board.is_insufficient_material():
        return 0
    
    total_evaluation = 0
    for i in range(CHESSBOARD_SIZE):
        for j in range(CHESSBOARD_SIZE):
            # A biblioteca python-chess armazena o tabuleiro como uma lista unidimensional de 64 casas.
            # A fórmula 'i * CHESSBOARD_SIZE + j' converte as coordenadas (i, j) em um índice linear que acessa a posição correspondente na lista.
            piece = board.piece_at(i * CHESSBOARD_SIZE + j)
            if piece:
                total_evaluation += evaluate_piece(piece, i, j)
    return total_evaluation


def get_best_move(depth, is_maximizing_player, board):
    best_value = -float('inf') if is_maximizing_player else float('inf')
    best_move_found = None

    for move in board.legal_moves:
        # Faz a jogada no tabuleiro
        board.push(move)  
        
        # Chama o minimax recursivamente para avaliar o valor do movimento.
        # Passa para o próximo nível da árvore de jogadas, alternando entre maximizador e minimizador.
        value = minimax(depth - 1, -float('inf'), float('inf'), not is_maximizing_player, board)
        
        # Reverte a jogada, voltando ao estado anterior do tabuleiro (backtracking)
        board.pop()  

        # Atualiza o melhor valor e a melhor jogada.
        if is_maximizing_player and value > best_value:
            best_value = value
            best_move_found = move

        elif not is_maximizing_player and value < best_value:
            best_value = value
            best_move_found = move

    return best_move_found


def minimax(depth, alpha, beta, is_maximizing_player, board):
    # Quando a profundidade chegar a 0, retorna o valor do tabuleiro
    if depth == 0:
        return -evaluate_board(board, current_depth = depth)

    # Se for a vez do jogador maximizador
    if is_maximizing_player:
        # Inicializa o melhor valor com um número muito baixo (representando o pior possível)
        best_move = -9999
        
        for move in board.legal_moves:
            board.push(move)  # Faz a jogada no tabuleiro
            
            # Chama recursivamente minimax para o próximo nível da árvore, com profundidade diminuída.
            # Alterna para o jogador minimizador.
            best_move = max(best_move, minimax(depth - 1, alpha, beta, not is_maximizing_player, board))
            
            board.pop()  # Reverte a jogada, voltando ao estado anterior do tabuleiro
            
            # Atualiza a poda alfa: o valor de alfa será o maior entre o valor atual e o melhor movimento encontrado
            alpha = max(alpha, best_move)
            
            # Poda: se o valor de beta for menor ou igual a alfa, não é necessário explorar mais 
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

from stockfish import Stockfish
import chess

sf = Stockfish(path='/home/rohit/Downloads/stockfish/stockfish-ubuntu-x86-64-avx2')
sf.set_elo_rating(3000)

board = chess.Board()
board.legal_moves

while True:
    mymove = input('Enter move:')
    board.push_san(mymove)
    sf.set_fen_position(board.fen())
    move = sf.get_best_move()
    move = board.parse_uci(move)
    compmove = board.san(move)
    board.push_san(compmove)
    print(board)
    print(board.fen())
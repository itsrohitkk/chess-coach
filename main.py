from stockfish import Stockfish

sf = Stockfish(path='/home/rohit/Downloads/stockfish/stockfish-ubuntu-x86-64-avx2')
sf.set_elo_rating(2000)
sf.get_board_visual()
while True:
    mymove = input()
    sf.make_moves_from_current_position([mymove])
    compmove = sf.get_best_move()
    sf.make_moves_from_current_position([compmove])
    print('Current moves: ',mymove,'   ',compmove)
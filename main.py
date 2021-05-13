from Classes.Board import Board


board = Board()
window = board.window
last_piece = None
while True:
    click = window.getMouse()
    piece, location = board.onclick(click)
    if piece == None:
        if last_piece:
            last_piece.clear_moves()
        last_piece = None
        continue
    elif piece.location == location:
        if piece == last_piece:
            last_piece.clear_moves()
            last_piece = None
        else:
            piece.onclick()
        last_piece = piece
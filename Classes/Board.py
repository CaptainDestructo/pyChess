from graphics import GraphWin

from Classes.BasePiece import Location
from Classes.Bishop import Bishop
from Classes.King import King
from Classes.Knight import Knight
from Classes.Pawn import Pawn
from Classes.Queen import Queen
from Classes.Rook import Rook

from Classes.BasePiece import getAllLocations


class Board:
    def __init__(self):

        self.locations = getAllLocations()

        window = GraphWin("Chess", 480, 480)

        self.pieces = {}
        self.pieces["wKing"] = King("white", window)
        self.pieces["wQueen"] = Queen("white", window)
        self.pieces["wcBishop"] = Bishop("white", window, "c")
        self.pieces["wfBishop"] = Bishop("white", window, "f")
        self.pieces["wbKnight"] = Knight("white", window, "b")
        self.pieces["wgKnight"] = Knight("white", window, "g")
        self.pieces["waRook"] = Rook("white", window, "a")
        self.pieces["whRook"] = Rook("white", window, "h")
        self.pieces["waPawn"] = Pawn("white", window, "a")
        self.pieces["wbPawn"] = Pawn("white", window, "b")
        self.pieces["wcPawn"] = Pawn("white", window, "c")
        self.pieces["wdPawn"] = Pawn("white", window, "d")
        self.pieces["wePawn"] = Pawn("white", window, "e")
        self.pieces["wfPawn"] = Pawn("white", window, "f")
        self.pieces["wgPawn"] = Pawn("white", window, "g")
        self.pieces["whPawn"] = Pawn("white", window, "h")

        self.pieces["bKing"] = King("black", window)
        self.pieces["bQueen"] = Queen("black", window)
        self.pieces["bcBishop"] = Bishop("black", window, "c")
        self.pieces["bfBishop"] = Bishop("black", window, "f")
        self.pieces["bbKnight"] = Knight("black", window, "b")
        self.pieces["bgKnight"] = Knight("black", window, "g")
        self.pieces["baRook"] = Rook("black", window, "a")
        self.pieces["bhRook"] = Rook("black", window, "h")
        self.pieces["baPawn"] = Pawn("black", window, "a")
        self.pieces["bbPawn"] = Pawn("black", window, "b")
        self.pieces["bcPawn"] = Pawn("black", window, "c")
        self.pieces["bdPawn"] = Pawn("black", window, "d")
        self.pieces["bePawn"] = Pawn("black", window, "e")
        self.pieces["bfPawn"] = Pawn("black", window, "f")
        self.pieces["bgPawn"] = Pawn("black", window, "g")
        self.pieces["bhPawn"] = Pawn("black", window, "h")

        self.window = window

    def onclick(self, click, justLoc=False):
        x = click.x
        y = click.y
        failed = True
        for location in self.locations:
            if x in location.range_x and y in location.range_y:
                if justLoc:
                    return location
                failed = False
                break
        if failed:
            raise ValueError(f"Couldn't find location containing ({x}, {y})")
        for piece in self.pieces.values():
            if piece.location == location:
                return piece, location
        return None, location

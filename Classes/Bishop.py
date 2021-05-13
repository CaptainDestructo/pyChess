from Classes.BasePiece import BasePiece, Location, getAllLocations
from typing import List


class Bishop(BasePiece):
    def __init__(self, color: str, window, col: str):
        super(Bishop, self).__init__(color, window, col)
        self.location = Location(col, 1 if self._color == "white" else 8)

    def set_valid_moves(self):
        _destination_rows = [8, 7, 6, 5, 4, 3, 2, 1]
        _destination_columns = ["a", "b", "c", "d", "e", "f", "g", "h"]
        self._valid_moves: List[Location] = []
        for row in _destination_rows:
            if row not in self.location._valid_rows:
                continue
            dev = row - self._row
            col = chr(ord(self._column) + dev)
            if col in self.location._valid_columns:
                location = Location(col, row)
                self._valid_moves.append(location)
            col = chr(ord(self._column) - dev)
            if col in self.location._valid_columns:
                location = Location(col, row)
                self._valid_moves.append(location)

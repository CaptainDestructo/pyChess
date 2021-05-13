from Classes.BasePiece import BasePiece, Location, getAllLocations
from typing import List


class King(BasePiece):
    def __init__(self, color: str, window, col: str = "e"):
        super(King, self).__init__(color, window, col)
        self.location = Location(col, 1 if self._color == "white" else 8)

    def set_valid_moves(self):
        _destination_rows = [self._row + dev for dev in range(-1, 2)]
        _destination_columns = [chr(ord(self._column) + dev) for dev in range(-1, 2)]
        self._valid_moves: List[Location] = []
        for row in _destination_rows:
            if row not in self.location._valid_rows:
                continue
            for column in _destination_columns:
                if column not in self.location._valid_columns:
                    continue
                location = Location(column, row)
                self._valid_moves.append(location)

from Classes.BasePiece import BasePiece, Location, getAllLocations
from typing import List


class Pawn(BasePiece):
    def __init__(self, color: str, window, col: str):
        super(Pawn, self).__init__(color, window, col)
        self.location = Location(col, 2 if self._color == "white" else 7)

    def set_valid_moves(self):
        if self._color == "white":
            _destination_rows = (
                [self._row + 1, self._row + 2] if self._row == 2 else [self._row + 1]
            )
        if self._color == "black":
            _destination_rows = (
                [self._row - 1, self._row - 2] if self._row == 7 else [self._row - 1]
            )

        _destination_columns = [
            self._column
        ]  # [chr(ord(self._column) + dev) for dev in range(-1, 2)]
        self._valid_moves: List[Location] = []
        for row in _destination_rows:
            if row not in self.location._valid_rows:
                continue
            for column in _destination_columns:
                if column not in self.location._valid_columns:
                    continue
                location = Location(column, row)
                self._valid_moves.append(location)

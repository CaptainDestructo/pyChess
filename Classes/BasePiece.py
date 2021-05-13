from graphics import Image, Point, Rectangle
from typing import List, Tuple
from collections import namedtuple


class Location:
    def __init__(self, column: str, row: int):
        if type(column) != str or type(row) != int:
            raise TypeError("Column must be char, row must be int")
            return
        self._valid_rows = [8, 7, 6, 5, 4, 3, 2, 1]
        self._valid_columns = ["a", "b", "c", "d", "e", "f", "g", "h"]

        if row not in self._valid_rows or column not in self._valid_columns:
            if row not in self._valid_rows:
                raise ValueError("Location rows must be in range 1 to 8")
            if column not in self._valid_columns:
                raise ValueError("Location columns must be in range a to h")
            return

        self.row: int = row
        self.column: str = column
        self.x = self._valid_columns.index(self.column) * 60 + 30
        self.y = self._valid_rows.index(self.row) * 60 + 30
        self.range_x = range(self.x - 30, self.x + 30)
        self.range_y = range(self.y - 30, self.y + 30)
        self.point = Point(self.x, self.y)

    def __eq__(self, other):
        if not isinstance(other, Location):
            return False
        elif self.x == other.x and self.y == other.y:
            return True
        else:
            return False


def getAllLocations():
    _valid_rows = [8, 7, 6, 5, 4, 3, 2, 1]
    _valid_columns = ["a", "b", "c", "d", "e", "f", "g", "h"]
    _all_locations = []
    for row in _valid_rows:
        for column in _valid_columns:
            location = Location(column, row)
            _all_locations.append(location)

    return _all_locations


class BasePiece:
    def __init__(self, color: str, window, col=None):
        _color = color.lower()
        if _color not in ["white", "black"]:
            raise TypeError("Must specify white or black for color")
            return
        self.window = window
        self._color: str = _color
        self._filename: str = f"images/{type(self).__name__}_{self._color}.png"
        self._image: Image = Image(Point(0, 0), self._filename)
        self._location: Location
        self._alive: bool = True
        self._valid_moves: List[Location] = []
        self.image.draw(self.window)
        self.move_squares = []

    @property
    def filename(self):
        return self._filename

    def get_image(self):
        return self._image

    def set_image(self, newImage: Image):
        if type(newImage) == type(self._image):
            self._image = newImage
        else:
            raise TypeError("newImage must be of type graphics.Image")

    def del_image(self):
        self._image: Image = Image(Point(0, 0), self._filename)

    image = property(get_image, set_image, del_image)

    def get_location(self):
        return self._location

    def set_location(self, newLocation: Location):
        self._location = newLocation
        self._row = newLocation.row
        self._column = newLocation.column
        last = self.image.getAnchor()
        self.image.move(0 - last.x, 0 - last.y)
        self.image.move(newLocation.x, newLocation.y)

    def del_location(self):
        pass

    location = property(get_location, set_location, del_location)

    @property
    def alive(self):
        return self._alive

    def kill(self):
        if self._alive:
            self._alive = False
            self.image.undraw()
        else:
            raise RuntimeError("Cannot kill a piece that is not alive")

    def move(self, newLocation: Location):

        if newLocation in self.valid_moves:
            self.location = newLocation
        else:
            raise ValueError(
                f"You cannot move to the specified location {newLocation.column}, {newLocation.row}"
            )

    def set_valid_moves(self):
        """Each subclass must have this function to generate a list of valid moves"""
        pass

    @property
    def valid_moves(self):
        self.set_valid_moves()
        return self._valid_moves

    def onclick(self):
        if self.move_squares != []:
            return
        for location in self.valid_moves:
            a = Point(location.x - 30, location.y - 30)
            b = Point(location.x + 30, location.y + 30)
            rectangle = Rectangle(a, b)
            rectangle.setFill("blue")
            self.move_squares.append(rectangle)
        for move in self.move_squares:
            move.draw(self.window)

    def clear_moves(self):
        for move in self.move_squares:
            move.undraw()
        self.move_squares = []
from location import Location


class Piece:
    symbol = "."

    def __init__(self, location: Location):
        self.location = location

    def __str__(self):
        return self.symbol


class Wall(Piece):
    symbol = "#"


class Floor(Piece):
    symbol = "."


class Box(Piece):
    symbol = "X"


class Target(Piece):
    symbol = "o"



from direction import Direction
from location import Location
from piece import Piece


class Player(Piece):
    symbol = "@"

    def __init__(self, name, location: Location):
        super().__init__(location)
        self.name = name
        self.moves = 0

    def move(self, direction: Direction):
        self.moves += 1
        self.location.move(direction)
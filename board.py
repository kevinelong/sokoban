from location import Location
from piece import Floor


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.rows = []
        for row_index in range(height):
            row = []
            for column_index in range(width):
                row.append(Floor(Location(column_index, row_index)))
            self.rows.append(row)

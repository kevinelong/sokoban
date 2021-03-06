from direction import Direction


class Location:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move(self, direction: Direction):
        if direction == Direction.UP:
            self.y -= 1
        if direction == Direction.RIGHT:
            self.x += 1
        if direction == Direction.DOWN:
            self.y += 1
        if direction == Direction.LEFT:
            self.x -= 1
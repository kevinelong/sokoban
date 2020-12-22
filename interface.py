from direction import Direction


class Interface:
    def __init__(self, game):
        self.game = game

    @staticmethod
    def get_user_input():
        print("Move which direction? ('wasd' or 'hjkl' keys)")
        value = input().strip().lower()
        if value in ['w', 'k']:
            return Direction.UP

        if value in ['d', 'l']:
            return Direction.RIGHT

        if value in ['s', 'j']:
            return Direction.DOWN

        if value in ['a', 'h']:
            return Direction.LEFT

    def __str__(self):
        output = f"MOVES: {self.game.player.moves}\n"
        for row_index in range(self.game.board.height):
            for column_index in range(self.game.board.width):
                output += " " + str(self.game.board.rows[row_index][column_index])
            output += "\n"
        return output

    def show(self):
        print(self)
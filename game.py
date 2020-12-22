from board import Board
from interface import Interface
from location import Location
from piece import Piece, Floor, Wall, Box, Target
from player import Player
from data import DATA


class Game:
    def __init__(self):
        self.playing = True
        self.board_width = 19
        self.board_height = 11
        self.player = Player("BOB", Location(self.board_width + 1 // 2, self.board_height + 1 // 2))
        self.board = Board(self.board_width, self.board_height)
        self.piece_list = []
        self.user_input = ""
        self.populate()
        self.interface = Interface(self)  # can be replaced after game is created to override default text interface

    def place_piece(self, p: Piece):
        # TODO verify space is empty
        self.piece_list.append(p)

    def move_piece(self, piece, destination: Location):
        pass
        # TODO validate destination

    def populate(self):
        piece_map = {
            " ": Floor,
            "#": Wall,
            "$": Box,
            ".": Target,
            "@": Player
        }
        data = DATA["levels"][0]
        row_index = 0
        for line in data.split("\n"):
            if 0 == len(line.strip()):
                continue
            column_index = 0
            for c in line:
                location = Location(column_index, row_index)
                if c == "@":
                    self.player.location = location
                    self.place_piece(self.player)
                elif c != ' ':
                    kind = piece_map[c]
                    self.place_piece(kind(location))
                column_index += 1
            row_index += 1
        self.update_board()

    def update_board(self):
        self.board = Board(self.board_width, self.board_height)

        for p in self.piece_list:
            if p.location != self.player.location:
                self.board.rows[p.location.y][p.location.x] = p
        self.board.rows[self.player.location.y][self.player.location.x] = self.player

    @staticmethod
    def is_solved() -> bool:
        return False

    def display_state(self):
        self.interface.show()

    def update_state(self, move):
        self.player.move(move)
        self.update_board()

    def play(self):
        # game loop - infinite
        while self.playing:
            self.display_state()
            move = self.interface.get_user_input()
            self.update_state(move)

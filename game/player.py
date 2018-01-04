from game import Board_Position
from scrabble_solving_engine.GADDAG import GaddagState
class Player(object):
    def __init__(self, number, lexicon, empty_cell):
        self.number = number
        self.tiles = ['' for i in range(7)]
        self.tiles_left = {'a': 9, 'b': 2, 'c': 2, 'd': 4, 'e': 12, 'f': 2, 'g': 3, 'h': 2,
                           'i': 9, 'j': 1, 'k': 1, 'l': 4, 'm': 2, 'n': 6, 'o': 8, 'p': 2,
                           'q': 1, 'r': 6, 's': 4, 't': 6, 'u': 4, 'v': 2, 'w': 2, 'x': 1,
                           'y': 2, 'z': 1, ' ': 2}
        self.lexicon = lexicon
        self.empty_cell = empty_cell
    def make_move(self, gameboard):
    # Get all possible start locations
    None

    def get_anchors(self, row, gameboard):
        anchors = []
        game_row = gameboard[row]
        for i in range(15):
            if game_row[i] in self.empty_cell:
                if row != 0:
                    if gameboard[row - 1][i] not in self.empty_cell:
                        anchors.append(Anchor(1, Board_Position(gameboard[row - 1][i], row, i)))
                if row != 15:
                    if gameboard[row + 1][i] not in self.empty_cell:
                        anchors.append(Anchor(3, Board_Position(gameboard[row + 1][i], row, i)))
                if i != 0:
                    if game_row[i - 1] not in self.empty_cell:
                        anchors.append(Anchor(0, Board_Position(game_row[i - 1], row, i)))
                if i != 15:
                    if game_row[i + 1] not in self.empty_cell:
                        anchors.append(Anchor(2, Board_Position(game_row[i + 1], row, i)))

        return anchors

        def Gen(pos, word, rack, state):
            if state.letter =

        def GoOn(pos, L, word, rack, new_arc, old_arc):

"""
    def get_all_moves(self, anchors, gameboard):
        root = self.lexicon.root
        letter_pos_dict = {}
        for anchor in anchors:
            # Use anchor letter, and search down every branch
            if anchor.direction == 0:
                anchor_letter = gameboard[anchor.position.x - 1][anchor.position.y]
            elif anchor.direction == 1:
                anchor_letter = gameboard[anchor.position.x][anchor.position.y - 1]
            elif anchor.direction == 2:
                anchor_letter = gameboard[anchor.position.x + 1][anchor.position.y]
            elif anchor.direction == 3:
                anchor_letter = gameboard[anchor.position.x][anchor.position.y + 1]
"""

class Move(object):
    def __init__(self, letter_pos_dict):
        self.lpd = letter_pos_dict

class Anchor(object):
    # direction = 0 is left
    # direction = 1 is up
    # direction = 2 is right
    # direction = 3 is down
    def __init__(self, direction, position):
        self.direction = direction
        self.position = position
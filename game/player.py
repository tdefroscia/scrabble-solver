from game import Board_Position
from scrabble_solving_engine.GADDAG import next_arc

"""
This is the class describing the scrabble player.

Attributes:
    number: whether the player is first (0) or second (1)
    rack: list of tiles that the player has
    tiles_left: the tiles left in the game in the player's point of view. Note
                that this is different from the actual tiles left. A player
                does not know the tiles which the other player has.
    lexicon: gaddag representing the entire scrabble dictionary
    empty_cell: hash set of representation of empty tiles on the board
    anchors: list of Board_Positions of letters adjacent to tiles already on the board
    
Methods:
    The general structure of this algorithm is this:
    1) From the present state of the gameboard, find all anchor squares
       Board -> anchors (get_anchors)
    2) Using the anchors, rack tiles, gaddag, and the board, generate all moves
       anchors + rack + gaddag + board -> moves (find_all_moves)
    3) From all the moves and the board, we pick the best move.
       moves + board -> move
    
    get_anchors:
    
    find_all_moves:
    
    gen:
    
    go_on:
"""
class Player(object):
    def __init__(self, number, lexicon, empty_cell):
        self.number = number
        self.rack = ['' for i in range(7)]
        self.tiles_left = {'a': 9, 'b': 2, 'c': 2, 'd': 4, 'e': 12, 'f': 2, 'g': 3, 'h': 2,
                           'i': 9, 'j': 1, 'k': 1, 'l': 4, 'm': 2, 'n': 6, 'o': 8, 'p': 2,
                           'q': 1, 'r': 6, 's': 4, 't': 6, 'u': 4, 'v': 2, 'w': 2, 'x': 1,
                           'y': 2, 'z': 1, ' ': 2}
        self.lexicon = lexicon
        self.empty_cell = empty_cell

    def gen_move(self, gameboard):
        anchors = self.get_anchors(gameboard)
        moves = self.get_all_across_moves(gameboard, anchors)
        gameboard_transpose = [[gameboard[j][i] for j in range(15)] for i in range(15)]
        moves.append(self.get_all_moves(gameboard_transpose, anchors))
        return self.get_best_move(moves, gameboard)

    def get_all_across_moves(self, gameboard, anchors):
        for anchor in anchors:
            self.gen(anchor, '', self.rack, self.lexicon.root_arc)
    def get_best_move(self, moves, gameboard):



    def score_move(self, move, gameboard):



    def get_anchors(self, gameboard):
        anchors = []
        for row in range(15):
            game_row = gameboard[row]
            for i in range(15):
                if game_row[i] in self.empty_cell:
                    if row != 0:
                        if gameboard[row - 1][i] not in self.empty_cell:
                            anchors.append(Board_Position(gameboard[row - 1][i], row, i))
                    if row != 15:
                        if gameboard[row + 1][i] not in self.empty_cell:
                            anchors.append(Board_Position(gameboard[row + 1][i], row, i))
                    if i != 0:
                        if game_row[i - 1] not in self.empty_cell:
                            anchors.append(Board_Position(game_row[i - 1], row, i))
                    if i != 15:
                        if game_row[i + 1] not in self.empty_cell:
                            anchors.append(Board_Position(game_row[i + 1], row, i))
        return anchors


    def rack_is_not_empty(self):
        for letter in self.rack:
            if letter != '':
                return True
        return False

    def gen(self, pos, word, rack, arc):
        if pos.letter not in self.empty_cell:
            self.go_on(pos, pos.letter, word, rack, next_arc(arc, pos.letter), arc)
        elif self.rack_is_not_empty():
            for i in range(len(rack)):
                # get allowed letters on the square
                if rack[i] == ' ':

                if rack[i] != '':
                    next_rack = rack
                    next_rack[i] = ''
                    self.go_on(pos, rack[i], word, next_rack, next_arc(arc, rack[i]), arc)


    def go_on(self, leftmost, pos, letter, word, rack, new_arc, old_arc):


class Move(object):
    def __init__(self, start_pos, word, horizontal):
        self.start_pos = start_pos
        self.word = word
        self.horizontal = horizontal

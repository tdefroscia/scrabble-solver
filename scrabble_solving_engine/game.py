from scrabble_solving_engine.GADDAG import GADDAG

class Game(object):
    tile_points = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4,
                   'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3,
                   'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8,
                   'y': 4, 'z': 10, ' ': 0}

    empty_cell = {'*', '0', '2', '3', '@'}
    word_multipliers = {'*': 3, '@': 2, '0': 1}
    letter_multipliers = {'0': 1, '2': 2, '3': 3}

    def __init__(self, lexicon):
        self.player_turn = 0
        self.player1_score = 0
        self.player2_score = 0
        self.tiles_left = {'a': 9, 'b': 2, 'c': 2, 'd': 4, 'e': 12, 'f': 2, 'g': 3, 'h': 2,
                           'i': 9, 'j': 1, 'k': 1, 'l': 4, 'm': 2, 'n': 6, 'o': 8, 'p': 2,
                           'q': 1, 'r': 6, 's': 4, 't': 6, 'u': 4, 'v': 2, 'w': 2, 'x': 1,
                           'y': 2, 'z': 1, ' ': 2}

        self.game_board = [['*', '0', '0', '2', '0', '0', '0', '*', '0', '0', '0', '2', '0', '0', '*'],
                           ['0', '@', '0', '0', '0', '3', '0', '0', '0', '3', '0', '0', '0', '@', '0'],
                           ['0', '0', '@', '0', '0', '0', '2', '0', '2', '0', '0', '0', '@', '0', '0'],
                           ['2', '0', '0', '@', '0', '0', '0', '2', '0', '0', '0', '@', '0', '0', '2'],
                           ['0', '0', '0', '0', '@', '0', '0', '0', '0', '0', '@', '0', '0', '0', '0'],
                           ['0', '3', '0', '0', '0', '3', '0', '0', '0', '3', '0', '0', '0', '3', '0'],
                           ['0', '0', '2', '0', '0', '0', '2', '0', '2', '0', '0', '0', '2', '0', '0'],
                           ['*', '0', '0', '2', '0', '0', '0', '@', '0', '0', '0', '2', '0', '0', '*'],
                           ['0', '0', '2', '0', '0', '0', '2', '0', '2', '0', '0', '0', '2', '0', '0'],
                           ['0', '3', '0', '0', '0', '3', '0', '0', '0', '3', '0', '0', '0', '3', '0'],
                           ['0', '0', '0', '0', '@', '0', '0', '0', '0', '0', '@', '0', '0', '0', '0'],
                           ['2', '0', '0', '@', '0', '0', '0', '2', '0', '0', '0', '@', '0', '0', '2'],
                           ['0', '0', '@', '0', '0', '0', '2', '0', '2', '0', '0', '0', '@', '0', '0'],
                           ['0', '@', '0', '0', '0', '3', '0', '0', '0', '3', '0', '0', '0', '@', '0'],
                           ['*', '0', '0', '2', '0', '0', '0', '*', '0', '0', '0', '2', '0', '0', '*']]
        self.lexicon = lexicon

    def validate_move(self, move):
        # Check that all tiles are in valid-locations
        # make sure tiles are not being placed on a covered square
        for tile in move:

        # make sure tile is not being placed out of bounds
        # make sure tiles are all in a line (vertical or horizontal)
        # Check that all words formed are valid
        return move

    def check_locations(self, move):
        None

    def check_lexicon(self, word):

        None

    def check_horizontal(self, move):
        None

    def check_vertical(self, move):
        None

    def update_board(self, move):
        None

class Board_Position(object):
    def __init__(self, letter, x, y):
        self.letter = letter
        self.x = x
        self.y = y

fd = open('dictionary.txt', 'r')
words_list = fd.read().split('\n')
fd.close()
lexicon = Gaddag()

for word in words_list:
    lexicon.add_word(word)

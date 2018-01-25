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
        self.valid_letters = [[{'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                                'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'} for i in range(15)] for j in range(15)]

    def cross_check(self, move):
        for pos in move:
            if pos.y != 0:
                if self.game_board[pos.x][pos.y - 1] in self.empty_cell:
                    self.update_valid_letters(pos.x, pos.y - 1, pos.letter)
            if pos.y != 14:
                if self.game_board[pos.x][pos.y + 1] in self.empty_cell:
                    self.update_valid_letters(pos.x, pos.y + 1, pos.letter)
            if pos.x != 0:
                if self.game_board[pos.x - 1][pos.y] in self.empty_cell:
                    self.update_valid_letters(pos.x - 1, pos.y, pos.letter)
            if pos.x != 14:
                if self.game_board[pos.x + 1][pos.y] in self.empty_cell:
                    self.update_valid_letters(pos.x + 1, pos.y, pos.letter)

    def update_valid_letters(self, row, col, letter):
        allowed_letters = self.lexicon.initialState.get_arc(letter).next_state.letter_set

        for ch in self.valid_letters[row][col]:
            if ch not in allowed_letters:
                self.valid_letters[row][col].remove(ch)

    def make_move(self, move):
        self.check_valid_move(move)
        self.make_move(move)
        self.cross_check(move)
        pass

    def check_valid_move(self, move):
        # Check that move is a word in the lexicon
        # Check that move is in valid board positions
        # Check that move is in valid_letters
        pass


class BoardPosition(object):
    def __init__(self, letter, x, y):
        self.letter = letter
        self.x = x
        self.y = y


def main():
    fd = open('dictionary.txt', 'r')
    words_list = fd.read().split('\n')
    fd.close()
    lexicon = GADDAG()

    for word in words_list:
        lexicon.add_word(word)


if __name__ == '__main__':
    main()

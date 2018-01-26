import unittest
from scrabble_solving_engine.GADDAG import GADDAG

class TestWords(unittest.TestCase):

    '''
    Iterate starting from a single arc until a terminal flag and check that the letters form a word
    continue for all arcs
    '''

    #def test_one_word_dictionary(self):
     #   self.assertTrue(test_valid_gaddag('one_word_test.txt'))
    def test_small_dictionary(self):
        self.assertTrue(test_valid_gaddag('small_test.txt'))
    #def test_full_dictionary(self):
     #   self.assertTrue(test_valid_gaddag('dictionary.txt'))

def test_valid_gaddag(dict_file):
    gaddag = GADDAG(dict_file)
    words_list = []
    get_all_words(gaddag.initialState, words_list, '')
    print(words_list)
    words_list = list(map(correct_word_order, words_list))
    with open(dict_file) as f:
        dictionary = f.read().split()
        for word in words_list:
            if word not in dictionary:
                print(word)
                return False
    return True


def get_all_words(current_state, word_list, current_word):
    if len(current_state.arcs) == 0:
        word_list.append(current_word)
    for arc in current_state.arcs:
        if arc.is_end and len(arc.next_state.arcs) != 0:
            word_list.append(current_word)
        get_all_words(arc.next_state, word_list, current_word + arc.letter)


def correct_word_order(word):
    real_word = ''
    rev = 1
    for char in word:
        if char == '|':
            rev = 0
        else:
            if rev:
                real_word = char + real_word
            else:
                real_word += char
    return real_word


if __name__ == '__main__':
    unittest.main()
import unittest
from scrabble_solving_engine.GADDAG import GADDAG

class TestWords(unittest.TestCase):

    '''

        Iterate starting from a single arc until a terminal flag and check that the letters form a word
        continue for all arcs

    '''

    def testValidWord(self):
        testWord = ""
        gaddag = GADDAG('one_word_test.txt')
        for arc in gaddag.initialState.arcs:
            if arc.letter == "|":
                # Reverse the test word
            if arc.is_end:
                return self.checkWord(testWord)

    @staticmethod
    def checkWord(word, filename):
        with open(filename) as f:
            dictionary = f.read().split()
        return word in dictionary

if __name__ == '__main__':
    unittest.main()
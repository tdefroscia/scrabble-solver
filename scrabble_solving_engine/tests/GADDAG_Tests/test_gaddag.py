import unittest
from scrabble_solving_engine.GADDAG import GADDAG

class TestGaddag(unittest.TestCase):
    def test_one_word(self):
        gaddag = GADDAG('one_word_test.txt')
        self.assertEqual(gaddag.initialState.letter_set, {'c', 'a', 'r', 'e'})
        self.assertEqual(gaddag.initialState.arcs[0].letter \
                         + ' ' + gaddag.initialState.arcs[0].next_state.arcs[0].letter \
                         + ' ' + gaddag.initialState.arcs[0].next_state.arcs[0].next_state.arcs[0].letter \
                         + ' ' + gaddag.initialState.arcs[0].next_state.arcs[0].next_state.arcs[0]\
                         .next_state.arcs[0].letter,
                         'e r a c')
        self.assertEqual(gaddag.initialState.arcs[1].letter
              + ' ' + gaddag.initialState.arcs[1].next_state.arcs[0].letter
              + ' ' + gaddag.initialState.arcs[1].next_state.arcs[0].next_state.arcs[0].letter
              + ' ' + gaddag.initialState.arcs[1].next_state.arcs[0].next_state.arcs[0].next_state.arcs[0].letter
              + ' ' + gaddag.initialState.arcs[1].next_state.arcs[0].next_state.arcs[0].next_state.arcs[0]\
              .next_state.arcs[0].letter,
              'r a c | e')
        self.assertEqual(gaddag.initialState.arcs[2].letter
              + ' ' + gaddag.initialState.arcs[2].next_state.arcs[0].letter
              + ' ' + gaddag.initialState.arcs[2].next_state.arcs[0].next_state.arcs[0].letter
              + ' ' + gaddag.initialState.arcs[2].next_state.arcs[0].next_state.arcs[0].next_state.arcs[0].letter
              + ' ' + gaddag.initialState.arcs[2].next_state.arcs[0].next_state.arcs[0].next_state.arcs[0]\
              .next_state.arcs[0].letter,
              'a c | r e')
        self.assertEqual(gaddag.initialState.arcs[3].letter
                        + ' ' + gaddag.initialState.arcs[3].next_state.arcs[0].letter
              + ' ' + gaddag.initialState.arcs[3].next_state.arcs[0].next_state.arcs[0].letter
              + ' ' + gaddag.initialState.arcs[3].next_state.arcs[0].next_state.arcs[0].next_state.arcs[0].letter
              + ' ' + gaddag.initialState.arcs[3].next_state.arcs[0].next_state.arcs[0].next_state.arcs[0]\
              .next_state.arcs[0].letter,
              'c | a r e')


def dictionary():
    print("started")
    GADDAG('dictionary.txt')
    print("done")


if __name__ == '__main__':
    unittest.main()
    dictionary()

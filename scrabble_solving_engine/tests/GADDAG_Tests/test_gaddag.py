from scrabble_solving_engine.GADDAG import GADDAG

def test_one():
    gaddag = GADDAG('one_word_test.txt')
    print(gaddag.initialState.letter_set)
    print(gaddag.initialState.arcs[0].letter + ' ' + gaddag.initialState.arcs[0].next_state.arcs[0].letter + ' ' + gaddag.initialState.arcs[0].next_state.arcs[0].next_state.arcs[0].letter + ' ' + str(gaddag.initialState.arcs[0].next_state.arcs[0].next_state.arcs[0].next_state.letter_set))
    print(gaddag.initialState.arcs[1].letter + ' ' + gaddag.initialState.arcs[1].next_state.arcs[0].letter + ' ' + gaddag.initialState.arcs[1].next_state.arcs[0].next_state.arcs[0].letter + ' ' + gaddag.initialState.arcs[1].next_state.arcs[0].next_state.arcs[0].next_state.arcs[0].letter + ' ' + str(gaddag.initialState.arcs[1].next_state.arcs[0].next_state.arcs[0].next_state.arcs[0].next_state.letter_set))
    print(gaddag.initialState.arcs[2].letter + ' ' + gaddag.initialState.arcs[2].next_state.arcs[0].letter + ' ' + gaddag.initialState.arcs[2].next_state.arcs[0].next_state.arcs[0].letter + ' ' + gaddag.initialState.arcs[2].next_state.arcs[0].next_state.arcs[0].next_state.arcs[0].letter + ' ' + str(gaddag.initialState.arcs[2].next_state.arcs[0].next_state.arcs[0].next_state.arcs[0].next_state.letter_set))
    print(gaddag.initialState.arcs[3].letter + ' ' + gaddag.initialState.arcs[3].next_state.arcs[0].letter + ' ' + gaddag.initialState.arcs[3].next_state.arcs[0].next_state.arcs[0].letter + ' ' + gaddag.initialState.arcs[3].next_state.arcs[0].next_state.arcs[0].next_state.arcs[0].letter + ' ' + str(gaddag.initialState.arcs[3].next_state.arcs[0].next_state.arcs[0].next_state.arcs[0].next_state.letter_set))

def dictionary():
    print("started")
    GADDAG('dictionary.txt')
    print("done")

if __name__ == '__main__':
    test_one()
    dictionary()

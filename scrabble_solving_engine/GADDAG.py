class GADDAG(object):
    def __init__(self, file_name):
        self.root_arc = Arc("", GaddagState(), False)
        self.initialState = self.root_arc.next_state
        self.create_gaddag(file_name)

    """
    Method used in initialization. Creates GADDAG from words in specified file.
    Expected format of the file is one word per line.

    Parameters:
        file_name: string with correct filepath

    Returns:
        Nothing
    """

    def create_gaddag(self, file_name):
        fd = open(file_name, 'r')
        words_list = fd.read().split('\n')
        fd.close()

        for word in words_list:
            self.add(word)

    """
    Adds a single word to the GADDAG and also performs partial minimization
    in order to be more space efficient.

    Parameters:
        word: string representing word that needs to be added

    Returns:
        Nothing
    """

    def add(self, word):
        n = len(word)
        st = self.initialState

        # creates path for word[n-1],word[n-2],...,word[0]
        for i in range(n - 1, 1, -1):
            st = add_arc(st, word[i])
        add_final_arc(st, word[1], word[0])

        # creates path for word[n-2],word[n-3],...word[0],'|',word[n]
        st = self.initialState
        for i in range(n - 2, -1, -1):
            st = add_arc(st, word[i])
        st = add_final_arc(st, '|', word[n - 1])

        # creates remaining paths and also performs partial minimization
        for m in range(n - 3, -1, -1):
            forceSt = st
            st = self.initialState
            for i in range(m, -1, -1):
                st = add_arc(st, word[i])
            st = add_arc(st, '|')
            force_arc(st, word[m + 1], forceSt)


def next_arc(arc, letter):
    st = arc.next_state
    return st.get_arc(letter)

"""
Adds an arc from st for ch (if one does not already exist) and resets st to
the node this arc leads to.

Parameters:
    st: GaddagState to which arc is added
    ch: Character corresponding to the new arc

Returns:
    The newest state (or the one which already existed)
"""


def add_arc(st, ch):
    arc = st.get_arc(ch)
    if arc == 0:
        arc = Arc(ch, GaddagState(), False)
        st.arcs.append(arc)
        st.letter_set.add(ch)
    return arc.next_state


"""
Adds an arc from st for c1 (if one does not already exist) and adds c2 to
the letter set on this arc

Parameters:
    st: GaddagState to which arc is added
    c1: character corresponding to new arc
    c2: character corresponding to last arc
Returns:
    The newest state (or the one which already existed)
"""


def add_final_arc(st, c1, c2):
    arc = st.get_arc(c1)
    if arc == 0:
        arc = Arc(c1, GaddagState(), False)
        st.arcs.append(arc)
        st.letter_set.add(c1)
    next_state = arc.next_state
    next_arc = next_state.get_arc(c2)
    if next_arc == 0:
        next_state.letter_set.add(c2)
        next_state.arcs.append(Arc(c2, GaddagState(), True))
    else:
        next_arc.is_end = True
    return next_state


"""
Adds an arc from st for ch to fst (an error occurs if an arc from st for ch
already exists going to any other state)

Parameters:
    st: GaddagState to which arc is added
    ch: Character corresponding to the new arc
    fst: state to which we minimize gaddag
Returns:
    Nothing
"""


def force_arc(st, ch, fst):
    arc = st.get_arc(ch)
    if arc != 0:
        if arc.next_state != fst:
            Exception("An arc from st for ch already exists")
    else:
        st.arcs.append(Arc(ch, fst, False))


class Arc(object):
    def __init__(self, letter, next_state, is_end):
        self.letter = letter
        self.next_state = next_state
        self.is_end = is_end


class GaddagState(object):
    def __init__(self):
        self.arcs = []
        self.letter_set = set()

    def get_arc(self, ch):
        for arc in self.arcs:
            if arc.letter == ch:
                return arc
        return 0

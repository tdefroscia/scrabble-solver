class GaddagState(object):
    def __init__(self):
        self.arcs = dict()
        self.letter_set = set()

    def add_arc(self, char):
        """
        Add an arc from the current state for char if no such arc exists. 
        Returns the node this arc leads to.
        """
        if char in self.arcs:
            next_state = self.arcs[char]
        else:
            next_state = GaddagState()
            self.arcs[char] = next_state
        return next_state

    def add_final_arc(self, c1, c2):
        """
        Add an arc from the current state for c1 if no such arc exists and adds c2 
        to the letter set at that state. Returns the node this arc leads to.
        """
        if c1 in self.arcs:
            next_state = self.arcs[c1]
        else:
            next_state = GaddagState()
            self.arcs[c1] = next_state
        next_state.letter_set.add(c2)
        return next_state

    def force_arc(self, char, forced_state):
        """
        Add an arc from the current state for char to forced_state, raising an 
        exception if an arc for char already exists going to any other state.
        """
        if char in self.arcs:
            if not self.arcs[char] == forced_state:
                raise Exception('Arc for forced character already exists.')
        self.arcs[char] = forced_state
        
class Gaddag(object):
    def __init__(self):
        self.root = GaddagState()

    def add_word(self, word):
        n = len(word)
        state = self.root   

        #create path for n...1
        for i in range(n-1, 1, -1):
            state = state.add_arc(word[i])
        state.add_final_arc(word[1], word[0])

        state = self.root   

        #create path for n-1...1|n
        for i in range(n-2, -1, -1):
            state = state.add_arc(word[i])
        state = state.add_final_arc('|', word[-1])

        #partially minimize the remaining paths
        for m in range(n-3, -1, -1):   
            forced_state = state
            state = self.root
            for i in range(m, -1, -1):
                state = state.add_arc(word[i])
            state = state.add_arc('|')
            state.force_arc(word[m+1], forced_state)

file = open('dictionary.txt', 'r')
words_list = file.read().split('\n')
file.close()
gaddag = Gaddag()

for word in words_list:
    gaddag.add_word(word)
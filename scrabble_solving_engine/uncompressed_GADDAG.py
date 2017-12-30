class Node:
    def __init__(self, letter):
        self.letter = letter
        self.children = dict()

    def add_child(self, char):
        if char in self.children:
            return self.children[char]
        else:
            toReturn = Node(char)
            self.children[char] = toReturn
            return toReturn

class Gaddag:
    def __init__(self):
        self.root = Node("")

    def add_word(self, word):
        n = len(word)
        for i in range(0,n):
            node = self.root
            for j in range(i, -1, -1):
                node = node.add_child(word[j])
            node = node.add_child('/')
            for j in range(i+1, n):
                node = node.add_child(word[j])
        node.add_child('')

file = open('dictionary.txt', 'r')
words_list = file.read().split('\n')
file.close()
gaddag = Gaddag()

for word in words_list:
    gaddag.add_word(word)

class dawgNode:
    def __init__(self, edges=[], termNode=0):
        self.edges = edges
        self.termNode = termNode
class dawgEdge:
    def __init__(self, letter, endNode):
        self.letter = letter
        self.endNode = endNode

def dawgConstructor(node, line, i):
    # Needs to be done

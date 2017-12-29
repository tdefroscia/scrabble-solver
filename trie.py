
# coding: utf-8

# In[1]:


class trieNode:
    def __init__(self, letter, termNode=0, children=[]):
        self.letter = letter
        self.termNode = termNode
        self.children = children


# In[2]:


def trieConstructor(node, i, line):
    if (i > len(line)-1):
        node.termNode = 1
        return
    for child in node.children:
        if (child.letter == line[i]):
            return trieConstructor(child, i+1, line)
    node.children.insert(0, trieNode(line[i], termNode=0, children=[]))
    return trieConstructor(node.children[0], i+1, line)


# In[3]:


root = trieNode(None)
file = open("dictionary.txt", "r")
for line in file:
    trieConstructor(root, 0, line)
file.close()


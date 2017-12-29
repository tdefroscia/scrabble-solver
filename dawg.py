
# coding: utf-8

# In[2]:


class dawgNode:
    def __init__(self, edges=[], termNode=0):
        self.edges = edges
        self.termNode = termNode
class dawgEdge:
    def __init__(self, letter, endNode):
        self.letter = letter
        self.endNode = endNode


# In[ ]:


def dawgConstructor(node, line, i):
    if (i >= len(line) - 1):
        return
    for edge in node.edges:
        if (edge.letter == line[i]):
            return dawgConstructor(edge.node, line, i+1)
    node.edges.


# In[ ]:





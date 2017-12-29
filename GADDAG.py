
# coding: utf-8

# In[1]:





# In[2]:


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
        prevNode = None
        notFirst = 0
        for i in range(0,n):
            node = self.root
            for j in range(i, -1, -1):
                node = node.add_child(word[j])
            node = node.add_child('/')
            if (notFirst and (i+1 < n)):
                node.children[word[i+1]] = prevNode
            for j in range(i+1, n):
                if (notFirst == 0):
                    node = node.add_child(word[j])
                if (j == i+2):
                    prevNode = node
            notFirst = 1
        node.add_child('')


# In[3]:


file = open('dictionary.txt', 'r')
words_list = file.read().split('\n')
file.close()
gaddag = Gaddag()

for word in words_list:
    gaddag.add_word(word)


# In[ ]:





# In[4]:


len(words_list)


# In[ ]:





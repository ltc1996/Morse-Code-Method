# this class is created for morse -> letter


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word, alpha):
        node = self.root
        # print(node, word, alpha)
        for char in word:
            if char not in node.keys():
                node[char] = {}
            node = node[char]
        node['word'] = alpha

    def search(self, word) -> bool:
        node = self.root
        for char in word:
            if char not in node.keys():
                return False
            else:
                node = node[char]
        return node['word']

    def show(self):
        return self.root

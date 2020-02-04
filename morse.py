di = '·'
da = '-'

morse2alpha = {
    'A': di + da          ,
    'B': da + di + di + di,
    'C': da + di + da + di,
    'D': da + di + di     ,
    'E': di               ,
    'F': di + di + da + di,
    'G': da + da + di     ,
    'H': di + di + di + di,
    'I': di + di          ,
    'J': di + da + da + da,
    'K': da + di + da     ,
    'L': di + da + di + di,             # .-..
    'M': da + da          ,
    'N': da + di          ,
    'O': da + da + da     ,
    'P': di + da + da + di,
    'Q': da + da + di + da,
    'R': di + da + di     ,             # .-.
    'S': di + di + di     ,
    'T': da               ,
    'U': di + di + da     ,
    'V': di + di + di + da,
    'W': di + da + da     ,
    'X': da + di + di + da,
    'Y': da + di + da + da,
    'Z': da + da + di + di,
}


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word, alpha):
        node = self.root
        # print(node, word, alpha)
        for char in word:
            if char not in node.keys():
                node[char] = {}
            node = node[char]
        # print(node)
        node['word'] = alpha
        # print(alpha, 'over')
        # node[char] = morse2alpha[alpha]

    def search(self, word) -> bool:
        node = self.root
        for char in word:
            if char not in node.keys():
                return False
            else:
                node = node[char]
        # print(node)
        # print(node['word'])
        return node['word']

    def show(self):
        return self.root


alpha2morse = Trie()
for k, v in morse2alpha.items():
    alpha2morse.insert(v, k)

if __name__ == '__main__':
    print(alpha2morse.show())
    print(alpha2morse.search('·-·'))


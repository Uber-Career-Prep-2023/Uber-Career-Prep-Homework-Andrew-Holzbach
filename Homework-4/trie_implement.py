class Trie_node:
    def __init__(self):
        self.children = {}
        for ascci in range(97,123):
            self.children[chr(ascci)] = None
        self.valid_Word = False
    
class Trie:
    def __init__(self):
        self.root = Trie_node()

    def insert(self, word:str):
        current = self.root
        for letter in word:
            if current.children[letter] is None:
                current.children[letter] = Trie_node()
            current = current.children[letter]
        current.valid_Word = True
    
    def isValidWord(self, word:str) -> bool:
        current = self.root
        for letter in word:
            current = current.children[letter]
            if current is None:
                return False
        if current.valid_Word:
            return True
        else:
            return False
    
    def remove(self, word:str):
        current = self.root
        prior_nodes = []
        for letter in word:
            current = current.children[letter]
            if current is None:
                return "word not in trie"
            prior_nodes.append((current, letter))
        if not current.valid_Word:
            return  "word not in trie"
        current.valid_Word = False
        if any(current.children.values()):
            return 
        while prior_nodes:
            node, letter = prior_nodes.pop()
            del node.children[letter]
            if node.valid_Word or any(node.children.values()):
                return
            
                
        
my_trie = Trie()
my_trie.insert('hi')
my_trie.insert('he')
my_trie.insert('hello')
my_trie.insert('hell')
#my_trie.remove("hi")
my_trie.remove('hello')
#print(my_trie.isValidWord("hi"))
print(my_trie.isValidWord("hello"))
print(my_trie.isValidWord('hell'))
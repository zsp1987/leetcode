class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            node = current.children.get(char)
            if not node:
                node = TrieNode()
                current.children[char] = node
            current = node
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            node = current.children.get(char)
            if not node:
                return False
            current = node
        return current.is_end_of_word
    
    def start_with(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            node = current.children.get(char)
            if not node:
                return False
            current = node
        return True
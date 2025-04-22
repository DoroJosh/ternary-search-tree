from src.ternary_search_tree.node import Node


class TernarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, word):
        if not word:
            return
        self.root = self._insert(self.root, word, 0)

    def _insert(self, node, word, index):
        char = word[index]

        if node is None:
            node = Node(char)

        if char < node.char:
            node.left = self._insert(node.left, word, index)
        elif char > node.char:
            node.right = self._insert(node.right, word, index)
        else:
            if index + 1 < len(word):
                node.middle = self._insert(node.middle, word, index + 1)
            else:
                node.is_end_of_word = True
                print(f"Inserted: {word}")

        return node

    def search(self, word):
        if not word:
            return False
        return self._search(self.root, word, 0)

    def _search(self, node, word, index):
        if node is None:
            return False

        char = word[index]

        if char < node.char:
            return self._search(node.left, word, index)
        elif char > node.char:
            return self._search(node.right, word, index)
        else:
            if index == len(word) - 1:
                return node.is_end_of_word
            return self._search(node.middle, word, index + 1)

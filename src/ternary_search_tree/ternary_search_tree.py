from src.ternary_search_tree.node import Node


class TernarySearchTree:
    def __init__(self):
        """Initialize an empty Ternary Search Tree."""
        self.root = None

    def search(self, word):
        """
        Search for a word in the Ternary Search Tree.

        Args:
            word (str): The word to search for.

        Returns:
            bool: True if the word exists in the tree, False otherwise.
        """
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

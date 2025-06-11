"""
Node class for Ternary Search Tree.

Each node contains a character and pointers to left, middle, and right child nodes.
- `left` points to nodes with characters less than the current one.
- `middle` continues the word if the current character matches.
- `right` points to nodes with characters greater than the current one.

Attributes:
    char (str): The character stored in the node.
    left (Node): Left child.
    middle (Node): Middle child.
    right (Node): Right child.
    is_end_of_word (bool): True if the node marks the end of a word.
"""
class Node:
    def __init__(self, char):
        """
        Initialize a new node with a character.

        Args:
            char (str): A single character for this node.
        """
        self.char = char
        self.left = None
        self.middle = None
        self.right = None
        self.is_end_of_word = False

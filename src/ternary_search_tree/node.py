from typing import Optional

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
    """
        Initialize a new node with a character.

        Args:
            char (str): A single character for this node.
        """
    def _init_(self, char: str):
        self.char: str = char
        self.is_end_of_string: bool = False
        self.left: Optional["Node"] = None
        self.eq: Optional["Node"] = None
        self.right: Optional["Node"] = None
    

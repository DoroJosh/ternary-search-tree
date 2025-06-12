from typing import Optional, List

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
        self.char = char
        self.is_end_of_string: bool = False
        self.left: Optional["Node"] = None
        self.eq: Optional["Node"] = None
        self.right: Optional["Node"] = None

class TernarySearchTree:
    def __init__(self):
        """
        Initialize an empty Ternary Search Tree.
        """
        self.root: Optional[Node] = None  # The tree starts with no nodes

    def insert(self, word: str) -> None:
        """
        Public method to insert a word into the Ternary Search Tree.

        Args:
            word (str): The word to insert.
        """
        if word:  # Avoid inserting empty strings
            self.root = self._insert(self.root, word, 0)  # Begin insertion at the root

    def _insert(self, node: Optional[Node], word: str, index: int) -> Node:
        """
        Recursively insert characters of a word into the Ternary Search Tree.

        Args:
            node (Optional[Node]): The current node in the tree.
            word (str): The word being inserted.
            index (int): The index of the current character being inserted.

        Returns:
            Node: The updated node after inserting the character.
        """
        char = word[index]  # Get the current character to insert

        if node is None:
            node = Node(char)  # type: ignore # Create a new node if the current position is empty

        if char < node.char:
            # Go left if the character is less than the current node's character
            node.left = self._insert(node.left, word, index)

        elif char > node.char:
            # Go right if the character is greater than the current node's character
            node.right = self._insert(node.right, word, index)

        else:
            # If characters match, proceed to the next character in the word
            if index + 1 < len(word):
                # Continue insertion in the middle (eq) child
                node.eq = self._insert(node.eq, word, index + 1)
            else:
                # We've reached the last character; mark this node as the end of a word
                node.is_end_of_string = True

        return node  # Return the updated node
    
    
    def search(self, word:str) ->bool:
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

    def _search(self, node:Optional[Node], word:str, index:int):
        """
        Recursive helper function to search for a word in the tree.

        Args:
            node (Node): The current node in the traversal.
            word (str): The word being searched.
            index (int): The current character index in the word.

        Returns:
            bool: True if the word is found, False otherwise.
        """
        if node is None:
            return False

        char = word[index]

        if char < node.char:
            return self._search(node.left, word, index)
        elif char > node.char:
            return self._search(node.right, word, index)
        else:
            if index == len(word) - 1:
                return node.is_end_of_string
            return self._search(node.eq, word, index + 1)

    def autocomplete(self, prefix: str) -> List[str]:
        """
        Return all words in the TST that start with the given prefix.
        
        Returns:
        List[str]: A list of all matching words.
        """
        results: List[str] = []
        node = self._get_node(self.root, prefix, 0)
        if node:
            if node.is_end_of_string:
                results.append(prefix)  # Add the prefix itself if it's a complete word
            self._collect(node.eq, prefix, results) # Collect all suffixes from here
        return results

    def _get_node(
        self, node: Optional[Node], prefix: str, index: int
    ) -> Optional[Node]:
        if not node or not prefix:
            return None

        char = prefix[index]

        if char < node.char:
            return self._get_node(node.left, prefix, index)
        elif char > node.char:
            return self._get_node(node.right, prefix, index)
        else:
            if index == len(prefix) - 1:
                return node
            return self._get_node(node.eq, prefix, index + 1)

    def _collect(
        self, node: Optional[Node], prefix: str, results: List[str]
    ) -> None:
        if node:
            self._collect(node.left, prefix, results)

            if node.is_end_of_string:
                results.append(prefix + node.char)

            self._collect(node.eq, prefix + node.char, results)
            self._collect(node.right, prefix,results)  
    
    

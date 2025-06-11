from src.ternary_search_tree.node import Node


class TernarySearchTree:
    def __init__(self):
        """
    Initialize an empty Ternary Search Tree.

    Attributes:
        root (Node or None): The root node of the tree. Starts as None.
        size (int): The number of unique words stored in the tree.
        has_empty_string (bool): Tracks whether an empty string has been inserted.
    """ 
        self.root = None 
        self.size = 0 
        self.has_empty_string = False 

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
                return node.is_end_of_word
            return self._search(node.middle, word, index + 1)
        
    
    def insert(self, word):
        """
    Insert a word into the Ternary Search Tree.

    If the word is an empty string, it sets the has_empty_string flag and 
    increments the tree size (only once for the first insertion of an empty string).

    Args:
        word (str): The word to insert into the tree.
    """ 
        if word == "": 
            if not self.has_empty_string:
                self.has_empty_string = True
                self.size += 1
            return
        
        def _insert(node, word, index):
            """
    Recursively insert characters of a word into the Ternary Search Tree.

    Args:
        node (Node): The current node in the tree.
        word (str): The word being inserted.
        index (int): The current index of the character being processed.

    Returns:
        Node: The updated node after insertion.
    """
            c = word[index] 

            if node is None: 
                node = Node(c) 
                
            if c < node.char: 
                node.less_than = _insert(node.less_than, word, index) 

            elif c > node.char:
                node.larger_than = _insert(node.larger_than, word, index)

            else: 
                if index == len(word) - 1:
                    if not node.is_end:
                        node.is_end = True  # Set the current node as the end of a word
                        self.size += 1  
                else:
                    node.equal = _insert(node.equal, word, index + 1) # Continue to the next character as we did not reach the end of the word

            return node 
        
        self.root = _insert(self.root, word, 0) # The root of the tree is going to be the result of inserting a new word to the already existing root

# Printing function 
    def __str__(self):
        lines = []
        def _str(node, relation, prefix):  
            if node is None: # This means the node on the left, for example, is empty 
                return
            lines.append(f"{relation}{prefix}char: {node.char}, terminates: {node.is_end}")
            _str(node.less_than, '_lt: ', prefix + '  ')
            _str(node.equal, '_eq: ', prefix + '  ')
            _str(node.larger_than, '_gt: ', prefix + '  ')
        lines.append(f"terminates: {self.has_empty_string}")    
        if self.root: 
            lines.append(f"       char: {self.root.char}, terminates: {self.root.is_end}")
            _str(self.root.less_than, '_lt: ', '     ')
            _str(self.root.equal, '_eq: ', '     ')
            _str(self.root.larger_than, '_gt: ','     ')
            return '\n'.join(lines)
        else:
            return "The tree is empty." # Not specified by the professor on the tests, but I believe it's good to mention 

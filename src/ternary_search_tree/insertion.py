# Initializing the insertion attributes 
class Node: 
    def __init__(self, char): 
        self.char = char 
        self.less_than = None # Initially, the nodes from left, middle and right side are empty 
        self.equal = None
        self.larger_than = None 
        self.is_end = False # This attribute will verify if a word ended or not 

# Initializing the tree 
class TernarySearchTree: 
    def __init__(self): 
        self.root = None # This means we start the tree with no nodes 
        self.size = 0 
        self.has_empty_string = False 
    
    def insert(self, word): 
        if word == "": # Verify if it's an empty string  
            if not self.has_empty_string:
                self.has_empty_string = True
                self.size += 1
            return
        
        def _insert(node, word, index):
            c = word[index] # Current character we are trying to insert 

            if node is None: 
                node = Node(c) # If the node is empty, we make a new node 

            if c < node.char: 
                node.less_than = _insert(node.less_than, word, index) 

            elif c > node.char:
                node.larger_than = _insert(node.larger_than, word, index)

            else: # The char matches exactly the node's char 
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

# Test 
tst = TernarySearchTree() 
tst.insert('abc')
tst.insert('aqt')
print(tst)

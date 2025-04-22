from src.ternary_search_tree.ternary_search_tree import TernarySearchTree
from src.ternary_search_tree.node import Node

# Create an instance of TernarySearchTree
tree = TernarySearchTree()

# Words to insert
words = ["cat", "cap", "bat", "car", "ca"]

# Insert words into the tree
for word in words:
    tree.insert(word)

# To verify: you could run search() after insert like this:
for word in words:
    found = tree.search(word)
    print(f"{word}: {'Found' if found else 'Not found'}")

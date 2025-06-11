class BTreeNode:
    """A node in the binary search tree."""

    def __init__(self, string: str):
        self.string = string
        self.left = None
        self.right = None

    def insert(self, string: str):
        """Insert a string into the subtree rooted at this node."""
        if string == self.string:
            return  # No duplicates allowed
        elif string < self.string:
            if self.left is None:
                self.left = BTreeNode(string)
            else:
                self.left.insert(string)
        else:
            if self.right is None:
                self.right = BTreeNode(string)
            else:
                self.right.insert(string)

    def search(self, string: str) -> bool:
        """Search for a string in the subtree."""
        if string == self.string:
            return True
        elif string < self.string:
            return self.left is not None and self.left.search(string)
        else:
            return self.right is not None and self.right.search(string)

    def all_strings(self) -> list[str]:
        """Return all strings in the subtree (in-order)."""
        result = []
        if self.left:
            result.extend(self.left.all_strings())
        result.append(self.string)
        if self.right:
            result.extend(self.right.all_strings())
        return result

    def __len__(self) -> int:
        """Return the size of the subtree rooted at this node."""
        length = 1
        if self.left:
            length += len(self.left)
        if self.right:
            length += len(self.right)
        return length

    def _to_string(self, indent: str = '') -> str:
        """Return a string representation of the subtree."""
        repr_str = indent + repr(self)
        if self.left:
            repr_str += '\n' + self.left._to_string(indent + '  ')
        if self.right:
            repr_str += '\n' + self.right._to_string(indent + '  ')
        return repr_str

    def __repr__(self) -> str:
        return self.string


class BinarySearchTree:
    """A binary search tree for storing strings."""

    def __init__(self):
        self.root = None

    def insert(self, string: str):
        """Insert a string into the tree."""
        if self.root is None:
            self.root = BTreeNode(string)
        else:
            self.root.insert(string)

    def search(self, string: str) -> bool:
        """Search for a string in the tree."""
        return self.root is not None and self.root.search(string)

    def all_strings(self) -> list[str]:
        """Return all strings stored in the tree (in-order)."""
        return [] if self.root is None else self.root.all_strings()

    def __len__(self) -> int:
        """Return the number of strings in the tree."""
        return 0 if self.root is None else len(self.root)

    def __repr__(self) -> str:
        """Return a string representation of the tree."""
        return "empty tree" if self.root is None else self.root._to_string()


# Optional for benchmarking compatibility
BinarySearchTree.__name__ = "BinarySearchTree"

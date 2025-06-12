import unittest
from ternary_search_tree import TernarySearchTree

class TestTernarySearchTree(unittest.TestCase):
    
    def setUp(self):
        self.tree = TernarySearchTree()
        self.words = ["cat", "car", "dog", "deer", "deal", "apple"]
        for word in self.words:
            self.tree.insert(word)

    def test_insert_and_search(self):
        for word in self.words:
            self.assertTrue(self.tree.search(word))
        self.assertFalse(self.tree.search("cow"))
        self.assertFalse(self.tree.search("cap"))

    def test_empty_tree(self):
        empty_tree = TernarySearchTree()
        self.assertFalse(empty_tree.search("anything"))
        self.assertEqual(len(empty_tree), 0)

    def test_length(self):
        self.assertEqual(len(self.tree), len(set(self.words)))

    def test_all_strings(self):
        all_words = self.tree.all_strings()
        for word in self.words:
            self.assertIn(word, all_words)

if __name__ == '__main__':
    unittest.main()

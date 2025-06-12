import os
import unittest
from ternary_search_tree import TernarySearchTree


def load_words_from_file(relative_path: str) -> list[str]:
    """Helper function to load words from a file relative to this test file."""
    base_dir = os.path.dirname(__file__)  # Path to src/
    filepath = os.path.join(base_dir, relative_path)  # Path to src/data/filename.txt
    with open(filepath, "r") as file:
        return [line.strip() for line in file if line.strip()]


class TestTernarySearchTree(unittest.TestCase):
    """
    Unit tests for the TernarySearchTree class.
    """

    def setUp(self):
        """
        Set up test environment with a populated TST and test word lists.
        """
        self.ternary_search_tree = TernarySearchTree()
        self.words = load_words_from_file("data/insert_words.txt")
        self.non_existing = load_words_from_file("data/not_insert_words.txt")

        for word in self.words:
            self.ternary_search_tree.insert(word)

    def test_insert_and_search_existing_words(self):
        for word in self.words:
            self.assertTrue(self.ternary_search_tree.search(word), f"Word '{word}' should be found.")

    def test_search_non_existing_words(self):
        """
        Ensure that non-inserted words are not found in the TST.
        """
        for word in self.non_existing:
            self.assertFalse(
                self.ternary_search_tree.search(word), f"Word '{word}' should NOT be found."
            )

    def test_insert_duplicate_word(self):
        """
        Inserting a duplicate word should not affect its retrievability.
        """
        word = self.words[0] if self.words else "apple"
        self.ternary_search_tree.insert(word)
        self.assertTrue(self.ternary_search_tree.search(word))

    def test_empty_string_handling(self):
        """
        Searching for an empty string should always return False.
        """
        self.assertFalse(self.ternary_search_tree.search(""), "Empty string should not be found.")

    def test_autocomplete_basic(self):
        """
        Test autocomplete results for common prefixes.
        """
        prefix = "ba"
        expected = [w for w in self.words if w.startswith(prefix)]
        self.assertCountEqual(self.ternary_search_tree.autocomplete(prefix), expected)

        prefix = "app"
        expected = [w for w in self.words if w.startswith(prefix)]
        self.assertCountEqual(self.ternary_search_tree.autocomplete(prefix), expected)

    def test_autocomplete_no_results(self):
        """
        Autocomplete on a non-existent prefix should return an empty list.
        """
        self.assertEqual(self.ternary_search_tree.autocomplete("zzz"), [])


if __name__ == "__main__":
    unittest.main()

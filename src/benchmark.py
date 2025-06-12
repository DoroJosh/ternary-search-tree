import time
import random
import matplotlib.pyplot as plt

from src.ternary_search_tree.ternary_search_tree import TernarySearchTree
from src.ternary_search_tree.btree import BinarySearchTree


def load_words(filepath: str, limit: int = None) -> list[str]:
    """Load words from a text file."""
    with open(filepath, "r") as file:
        words = [line.strip().lower() for line in file if line.strip().isalpha()]
    if limit:
        words = words[:limit]
    return words


def benchmark_tree(TreeClass, words: list[str], step: int = 1000):
    insert_times = []
    search_times = []
    sizes = list(range(step, len(words) + 1, step))

    for size in sizes:
        sample = words[:size]
        tree = TreeClass()

        # Measure insert time
        start = time.perf_counter()
        for word in sample:
            tree.insert(word)
        end = time.perf_counter()
        insert_times.append(end - start)

        # Measure search time on 10% random sample
        search_sample = random.sample(sample, k=max(1, size // 10))
        start = time.perf_counter()
        for word in search_sample:
            tree.search(word)
        end = time.perf_counter()
        search_times.append(end - start)

        print(
            f"{TreeClass.__name__}: {size} words - Insert: {insert_times[-1]:.4f}s, Search: {search_times[-1]:.4f}s"
        )

    return sizes, insert_times, search_times


def plot_benchmark(sizes, insert_times1, search_times1, insert_times2, search_times2):
    plt.figure(figsize=(12, 5))

    # Insert Times
    plt.subplot(1, 2, 1)
    plt.plot(sizes, insert_times1, label="Ternary Search Tree", marker="o")
    plt.plot(sizes, insert_times2, label="Binary Search Tree", marker="x")
    plt.title("Insert Time")
    plt.xlabel("Number of Words")
    plt.ylabel("Time (seconds)")
    plt.legend()

    # Search Times
    plt.subplot(1, 2, 2)
    plt.plot(sizes, search_times1, label="Ternary Search Tree", marker="o")
    plt.plot(sizes, search_times2, label="Binary Search Tree", marker="x")
    plt.title("Search Time")
    plt.xlabel("Number of Words")
    plt.ylabel("Time (seconds)")
    plt.legend()

    plt.tight_layout()
    plt.savefig("benchmark_results.png")
    plt.show()


if __name__ == "__main__":
    word_file = "data/corncob_lowercase.txt"
    words = load_words(word_file, limit=10000)

    print("\nBenchmarking Ternary Search Tree (TST)...")
    sizes_tst, insert_tst, search_tst = benchmark_tree(TernarySearchTree, words)

    print("\nBenchmarking Binary Search Tree (BST)...")
    sizes_bst, insert_bst, search_bst = benchmark_tree(BinarySearchTree, words)

    plot_benchmark(sizes_tst, insert_tst, search_tst, insert_bst, search_bst)

import time
import random
from src.ternary_search_tree.ternary_search_tree import TernarySearchTree
from src.ternary_search_tree.btree import BTreeWrapper


def load_words(filepath: str, limit: int = None) -> list[str]:
    """Load words from a text file."""
    with open(filepath, "r") as file:
        words = [line.strip().lower() for line in file if line.strip().isalpha()]
    return words[:limit] if limit else words


def benchmark_tree(TreeClass, words: list[str], step: int = 1000):
    insert_times = []
    search_times = []
    sizes = list(range(step, len(words) + 1, step))

    for size in sizes:
        sample = words[:size]
        tree = TreeClass()

        # Insert timing
        start = time.perf_counter()
        for word in sample:
            tree.insert(word)
        end = time.perf_counter()
        insert_times.append(end - start)

        # Search timing
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


def save_results(filename, sizes, insert_times, search_times):
    import csv
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Size", "InsertTime", "SearchTime"])
        for s, i, sr in zip(sizes, insert_times, search_times):
            writer.writerow([s, i, sr])


if __name__ == "__main__":
    word_file = "data/corncob_lowercase.txt"
    words = load_words(word_file, limit=10000)

    print("\nBenchmarking Ternary Search Tree (TST)...")
    sizes_tst, insert_tst, search_tst = benchmark_tree(TernarySearchTree, words)
    save_results("benchmark/results/tst_benchmark.csv", sizes_tst, insert_tst, search_tst)

    print("\nBenchmarking B-Tree...")
    sizes_bt, insert_bt, search_bt = benchmark_tree(BTreeWrapper, words)
    save_results("benchmark/results/btree_benchmark.csv", sizes_bt, insert_bt, search_bt)

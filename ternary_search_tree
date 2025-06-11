import time
import random
from src.ternary_search_tree.ternary_search_tree import TernarySearchTree
from src.ternary_search_tree.btree import BTreeWrapper

import matplotlib.pyplot as plt


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

#Plotting the benchmark runs
def plot_benchmark(sizes, insert_times_dict, search_times_dict):
    plt.figure(figsize=(12, 5))

    # Insertion time plot
    plt.subplot(1, 2, 1)
    for label, times in insert_times_dict.items():
        plt.plot(sizes, times, label=label)
    plt.title("Insert Time vs. Number of Words")
    plt.xlabel("Number of Words")
    plt.ylabel("Insert Time (s)")
    plt.legend()
    plt.grid(True)

    # Search time plot
    plt.subplot(1, 2, 2)
    for label, times in search_times_dict.items():
        plt.plot(sizes, times, label=label)
    plt.title("Search Time vs. Number of Words")
    plt.xlabel("Number of Words")
    plt.ylabel("Search Time (s)")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig("benchmark/benchmark_plots.png") 
    plt.show()

plot_benchmark(
    sizes_tst,
    {
        "Ternary Search Tree": insert_tst,
        "Binary Search Tree": insert_bst,
        "B-Tree": insert_bt,
    },
    {
        "Ternary Search Tree": search_tst,
        "Binary Search Tree": search_bst,
        "B-Tree": search_bt,
    }
)

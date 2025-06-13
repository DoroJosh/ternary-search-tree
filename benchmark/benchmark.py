import time
import random 
import matplotlib.pyplot as plt
from src.ternary_search_tree import TernarySearchTree
from src.btree import BTreeWrapper 

def load_words(filepath: str, limit: int = None) -> list[str]:
    """Load words from a text file"""
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

        start = time.perf_counter()
        for word in sample:
            tree.insert(word)
        end = time.perf_counter()
        insert_times.append(end - start)

        search_sample = random.sample(sample, k=max(1, size // 10))
        start = time.perf_counter()
        for word in search_sample:
            tree.search(word)
        end = time.perf_counter()
        search_times.append(end - start)

        print(
            f"{TreeClass.__name__}: {size} words - Insert time is {insert_times[-1]:.4f}s - Search time is {search_times[-1]:.4f}s"
        )

    return sizes, insert_times, search_times


if __name__ == "__main__":
    word_file = "src/data/corncob_lowercase.txt"
    words = load_words(word_file, limit=10000)

    print("\nBenchmarking Ternary Search Tree (TST)")
    sizes_tst, insert_tst, search_tst = benchmark_tree(TernarySearchTree, words)

    print("\nBenchmarking BTree")
    sizes_bt, insert_bt, search_bt = benchmark_tree(BTreeWrapper, words)

    " Benchmarking visualization Insert"

    plt.plot(sizes_tst, insert_tst, label='TST Insert')
    plt.plot(sizes_bt, insert_bt, label='BTree Insert')
    plt.title('Benchmarking visualization - Time to insert vs Number of words')
    plt.xlabel('Number of words')
    plt.ylabel('Time (s)')
    plt.grid(True)
    plt.show()

    " Benchmarking visualization Search"    
    plt.plot(sizes_tst, search_tst, label='TST Insert')
    plt.plot(sizes_bt, search_bt, label='BTree Insert')
    plt.title('Benchmarking visualization - Time to search vs Number of words')
    plt.xlabel('Number of words')
    plt.ylabel('Time (s)')
    plt.grid(True)
    plt.show()
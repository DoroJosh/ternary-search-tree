# Complexity Notes

This document includes our conclusions about expected time and space complexity of our ternary search tree implementation, along with predicted scenarios (best, average and worse). 

---

### Expected time
The time complexity expected is linear O(n), where 'n' represents the size of the word, and the running time increases linarly with it. 

- Best case scenario: The tree is well balanced the checks are being done in the middle node. Time complexity is linear O(n). 
- Average case scenario: The tree is fairly balanced and the checks are still mostly being done in the middle node. Time complexity remains linear O(n). 
- Worse case scenario: The tree is unbalanced. The words included were inserted in a sorted order, causing excessive branching on the left and right nodes before reaching the middle. In this case, time complexity also depends on height of the tree (h), being represented as O(n * h). 

### Memory space complexity
The memory space complexity is linear O(n), where 'n' is the number of nodes. Each node stores one character on the left middle and right child.  

- Best case scenario: Many words share the same prefix, which leads to nodes being reused. The complexity is linear O(n). 
- Average case scenario: There is a moderate presence of words sharing the same prefix. Overall the complexity remains linear O(n).
- Worse case scenario: No word shares a prefix, which leads to a unique path for each word. The complexity will be multiplied by the average size (s) of the words. O(n * s). 

---

## Benchmark Results 
Benchmarking results show that our TST implementation does not exhibit linear time complexity for insert operations. This behavior may be attributed to inefficiencies or overhead in our manual implementation, and suggests that further optimization is needed.

<div align="center">
  <img src="https://github.com/DoroJosh/ternary-search-tree/blob/main/benchmark/plots/insert_benchmark.png?raw=true" width="450"><br>
  <b>Figure 1:</b> Insert time vs number of words 
</div>

<br>

<div align="center">
  <img src="https://github.com/DoroJosh/ternary-search-tree/blob/main/benchmark/plots/search_benchmark.png?raw=true" width="450"><br>
  <b>Figure 2:</b> Search time vs number of words 
</div>

<br>

When compared to the BTree from external package, our TST has consistently higher insertion times, which is expected. The BTree benefits from low-level optimizations and mature data structures. TST still demonstrates reasonably efficient performance for both insertion and search operations. This was further confirmed by executing the benchmark on HPC structure. 

Detailed performance results, including insert and search times at each scale, can be found in the file 'vsc/slurm-58227347.out'.

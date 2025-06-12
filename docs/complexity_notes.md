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

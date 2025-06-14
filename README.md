# ternary-search-tree
Hasselt University - 1st year Master of Statistics and Data Science

Project Concepts of Data Science 2024-2025: Implementation of a Ternary Search Tree in Python

Contributors: Dorothy Chepkoech (2469284) and Marilia Bezerra (2469866)

## Project Overview
A Ternary Search Tree is a type of trie (prefix tree) where each node has three children:
- **Left**: Points to characters that are less than the current node.
- **Middle**: Continues the word when the current character matches.
- **Right**: Points to characters greater than the current node.

TST is optimized for efficient **search** and **insert** operations on string data. A Ternary Search Tree is a hybrid between a binary search tree and a trie, offering efficient memory usage and fast string search operations particularly useful in applications like autocomplete, dictionary search, and spell checking.

## Features implemented
**Insert Operation**: Efficiently inserts strings into the TST.

**Search Operation**: Performs exact string searches within the tree.

**performance comparison**:Includes benchmarking against a Btree implementation using Btrees.OOBTree

## Dependencies
- Python 3.10.13

## Contribution Guidelines
- **Branching**: All feature development was done on feature branches.
- **Commit Message Format**: Use of conventional guidelines.
- **Pull Request**: Open pull requests should be reviewed before merging into the `development` branch.

## Implementation on HPC structure
- The script used to run this project on the HPC is available under the file name 'src/jobscript_tst.slurm'.
- To allow the a few packages to be used, a virtual environment (VE) was made. Additional information about this VE can be found on the file 'benchmark/vsc/requirements.txt'.

## Benchmark and complexity notes 
- Benchmark was done to analyze the TST's performance on insertion and search operations. This was done across increasing word volumes, and compared a B-Tree wrapper to analyze time complexity trends. this was done on the HPC structure, the results can be found under 'benchmark/vsc/slurm-58227347.out'. 

## Conclusion
Benchmarking revealed that the Ternary Search Tree (TST), though fully functional and capable of scaling with larger datasets, is notably slower than the B-Tree implementation in both insertion and search operations.These findings indicate that while TSTs are well-suited for applications focused on strings
such as prefix matching or autocomplete they may not be ideal for scenarios demanding high-speed performance. In such cases, B-Trees offer a more efficient alternative for both insert and search operations.
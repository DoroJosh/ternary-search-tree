# ternary-search-tree
Hasselt University - 1st year Master of Statistics and Data Science

Project Concepts of Data Science 2024-2025: Implementation of a Ternary Search Tree in Python

Contributors: Dorothy Chepkoech (2469284) and Marilia Bezerra (2469866)

## Project Overview
A Ternary Search Tree is a type of trie (prefix tree) where each node has three children:
- **Left**: Points to characters that are less than the current node.
- **Middle**: Continues the word when the current character matches.
- **Right**: Points to characters greater than the current node.

TST is optimized for efficient **search** and **insert** operations on string data. It is particularly useful when working with large dictionaries or predictive text systems. Benchmarking was also done do compare the performance of our TST with a BTree. 

## Implemented Features

###  Features in Progress:
- **Traverse**: Return all words in lexicographical order (to be implemented).

## Dependencies
- Python 3.10.13

## Contribution Guidelines
- **Branching**: All feature development was done on feature branches.
- **Commit Message Format**: Use of conventional guidelines.
- **Pull Request**: Open pull requests should be reviewed before merging into the `development` branch.

## Implementation on HPC structure
- The script used to run this project on the HPC is available under the file name 'src/jobscript_tst.slurm'. Note, in the script, the number of nodes and tasks were not specified because we used the default option (one node and one task). 
- To allow the packages matplotlib and OOBTree to be used, a virtual environment (VE) was made. Additional information about this VE can be found on the file 'benchmark/vsc/requirements.txt'.

## Complexity notes 
- Final considerations about time and space complexity are available on 'docs/compexity_notes.md'. 

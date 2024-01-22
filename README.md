[![Build Status](https://travis-ci.com/AladdinPersson/Algorithms-Collection-Python.svg?branch=master)](https://travis-ci.com/AladdinPersson/Algorithms-Collection-Python) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![codecov](https://codecov.io/gh/aladdinpersson/Algorithms-Collection-Python/branch/master/graph/badge.svg)](https://codecov.io/gh/aladdinpersson/Algorithms-Collection-Python)

# Algorithms Collection Python
Whenever I face an interesting problem I document the algorithm that I learned to solve it. The goals of this repository is to have clean, efficient and most importantly correct code.

:white_check_mark:: If the algorithm is tested  \
:small_red_triangle:: If the algorithm is untested

# Dynamic Programming
* :white_check_mark: [Knapsack 0/1](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/dynamic_programming/knapsack/knapsack_bottomup.py)  **- O(nC) Bottom-Up implementation (Loops)**
* :white_check_mark: [:movie_camera:](https://youtu.be/XmyxiSc3LKg)[Sequence Alignment](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/dynamic_programming/sequence_alignment.py) **- O(nm)**
* :white_check_mark: [:movie_camera:](https://youtu.be/dU-coYsd7zw)[Weighted Interval Scheduling](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/dynamic_programming/weighted_interval_scheduling.py) **- O(nlog(n))**

# Graph theory
* :white_check_mark: [Kahns Topological Sort](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/graphtheory/kahns-toposort/kahn_topological_ordering.py) **- O(n + m)**
* :white_check_mark: [Bellman-Ford Shortest Path](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/graphtheory/bellman-ford/bellman_ford.py) **- O(mn)**
* :small_red_triangle: [Floyd-Warshall Shortest Path](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/graphtheory/floyd-warshall/floyd-warshall.py) **- O(n<sup>3</sup>)**
* :white_check_mark: [Dijkstra Shortest Path](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/graphtheory/dijkstra/dijkstra.py) **- Naive implementation**
* :white_check_mark: [Dijkstra Shortest Path](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/graphtheory/dijkstra/heapdijkstra.py) **- O(mlog(n)) - Heap implementation**
* :small_red_triangle: [Karger's Minimum cut](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/graphtheory/kargers/kargermincut.py)
* :small_red_triangle: [Prim's Algorithm](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/graphtheory/prims/prim_naive.py) **- O(mn) Naive implementation**
* :white_check_mark: [Prim's Algorithm](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/graphtheory/prims/prim_heap.py) **- O(mlog(n)) Heap implementation**
* :small_red_triangle: [Kruskal's Algorithm](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/graphtheory/kruskal/kruskal.py) **- O(mn) implementation**
* :white_check_mark: [Kruskal's Algorithm](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/graphtheory/kruskal/kruskal_unionfind.py) **- O(mlog(n))**
* :white_check_mark: [Breadth First Search](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/graphtheory/breadth-first-search/BFS_queue_iterative.py) **- O(n + m) - Queue Implementation**
* :white_check_mark: [Depth First Search](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/graphtheory/depth-first-search/DFS_stack_iterative.py) **- O(n + m) - Stack Implementation**
* :white_check_mark: [Depth First Search](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/graphtheory/depth-first-search/DFS_recursive.py) **- O(n + m) - Recursive Implementation**

# Mathematics
### Algebra
* :small_red_triangle: [Karatsuba Multiplication](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/math/karatsuba/karatsuba.py) **- O(n<sup>1.585</sup>)** 
* :white_check_mark: [Intersection of two sets](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/math/intersection_of_two_sets/intersection_of_two_sets.py) **- O(nlog(n)) + O(mlog(m))** 
* :white_check_mark: [Union of two sets](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/math/union_of_two_sets/union_of_two_sets.py) **- O(nlog(n)) + O(mlog(m))** 

### Number Theory
* :small_red_triangle: [Pollard p-1 factorization](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/math/pollard_p1/pollard_p1.py)
* :small_red_triangle: [Euclidean Algorithm](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/math/euclid_gcd/euclid_gcd.py)  **- O(log(n))**
* :small_red_triangle: [Extended Euclidean Algorithm](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/math/extended_euclidean_algorithm/euclid_gcd.py)  **- O(log(n))**
* :small_red_triangle: [Sieve of Eratosthenes](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/math/sieve_of_eratosthenes/sieve_eratosthenes.py) **- O(nlog(log(n)))**
* :small_red_triangle: [Prime factorization](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/math/prime_factorization/primefactorization.py) **- O(sqrt(n))**

### Cryptography
* :white_check_mark: [Ceasar Cipher](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/cryptology/ceasar_shifting_cipher/ceasar_shift_cipher.py)
* :small_red_triangle: [Hill Cipher](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/cryptology/hill_cipher/hill_cipher.py)
* :small_red_triangle: [Vigenere Cipher](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/cryptology/vigenere_cipher/vigenere.py)*
* :small_red_triangle: [One time pad](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/cryptology/one_time_pad/one_time_pad.py)
* :small_red_triangle: [RSA-Algorithm](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/cryptology/RSA_algorithm/RSA.py)


### Numerical Methods
* :small_red_triangle: [Bisection Method](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/numerical_methods/bisection.py)
* :small_red_triangle: [(simple) Fixpoint iteration](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/numerical_methods/fixpoint.py)

# Other
* :white_check_mark: [Maintaining Median](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/other/median_maintenance.py) **- O(nlog(n))**
* :small_red_triangle: [Huffman Algorithm](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/other/Huffman/Huffman.py)
* :white_check_mark: [:movie_camera:](https://youtu.be/SmPxC8m0yIY)[Interval Scheduling](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/other/interval_scheduling.py) **- O(nlog(n))**
* :white_check_mark: [Binary Search](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/other/binarysearch.py) **- O(log(n))** 

# Sorting algorithms
*  :white_check_mark: [Bubble sort](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/sorting/bubblesort.py) **- O(n<sup>2</sup>)** 
*  :small_red_triangle: [Hope sort](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/sorting/hopesort.py) **- O(1), hopefully**
*  :white_check_mark: [Insertion sort](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/sorting/insertionsort.py) **- O(n<sup>2</sup>)** 
*  :white_check_mark: [Selection sort](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/sorting/selectionsort.py) **- O(n<sup>2</sup>)** 
*  :white_check_mark: [Merge sort](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/sorting/mergesort.py) **- O(nlog(n))** 
*  :white_check_mark: [Randomized Quick sort](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/sorting/randomized_quicksort.py) **- Average O(nlogn) (Input independent!)**
*  :white_check_mark: [Quick sort](https://github.com/aladdinpersson/Algorithms-Collection-Python/blob/master/Algorithms/sorting/quicksort.py) **- Average O(nlog(n))**

# Contributing
I appreciate feedback on potential improvements and/or if you see an error that I've made! Also if you would like to contribute then do a pull request with algorithm & tests! :)



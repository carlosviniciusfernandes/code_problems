# Quick Sort

Divide and Conquer! -> split the input into chunks and then solve things faster with small subsets

TLDR: It uses recursion in conjunction with pivot element used for "weak sorting", descending into a sorted tree like structure **that can O(nlogn) best case**

NOTE: Quick sort doesn't always sort quickly
If you have a reserve sorted array and takes the pivot as the last element, we will have the **worst possible case**, which will fall into **O(n²)**

[QuickSort](./kata-machine/src/day1/QuickSort.ts)

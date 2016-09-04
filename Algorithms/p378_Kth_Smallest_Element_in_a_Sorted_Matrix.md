Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.

Note: 
You may assume k is always valid, 1 ¡Ü k ¡Ü n2.

Solution:
1.pop smallest element (top-left) k-1 times, then return matrix[0][0].
time complexity: O(kn) (generally O(k(m+n)))
2.maintain a min heap of smallest elements from n columns (rows). pop k-1 times, then return heap[0]
time complexity: O(n+klgn) (generally O(n+klgn) or O(m+klgm))
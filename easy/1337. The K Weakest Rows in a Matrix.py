"""
You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

Example 1:

Input: mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
Output: [2,0,3]
Explanation: 
The number of soldiers in each row is: 
- Row 0: 2 
- Row 1: 4 
- Row 2: 1 
- Row 3: 2 
- Row 4: 5 
The rows ordered from weakest to strongest are [2,0,3,1,4].

Example 2:

Input: mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2
Output: [0,2]
Explanation: 
The number of soldiers in each row is: 
- Row 0: 1 
- Row 1: 4 
- Row 2: 1 
- Row 3: 1 
The rows ordered from weakest to strongest are [0,2,3,1].

Constraints:

m == mat.length
n == mat[i].length
2 <= n, m <= 100
1 <= k <= m
matrix[i][j] is either 0 or 1.
"""

# My solutions
# Runtime: 241 ms, faster than 37.55% of Python3 online submissions for The K Weakest Rows in a Matrix.
# Memory Usage: 14.3 MB, less than 50.33% of Python3 online submissions for The K Weakest Rows in a Matrix.
# Runtime O(n log n), Memory O(n)
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        cnt_soldiers = {index: item.count(1) for index, item in enumerate(mat)}
        sorted_soldiers = sorted(cnt_soldiers.items(), key=lambda item: item[1])
        
        return [item[0] for item in sorted_soldiers[:k]]


# Best solutions
# Runtime: 233 ms, faster than 42.66% of Python3 online submissions for The K Weakest Rows in a Matrix.
# Memory Usage: 14.1 MB, less than 88.27% of Python3 online submissions for The K Weakest Rows in a Matrix.
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m = len(mat)
        rows = sorted(range(m), key=lambda item: mat[item])
        return rows[:k]


# Runtime: 286 ms, faster than 14.32% of Python3 online submissions for The K Weakest Rows in a Matrix.
# Memory Usage: 14.1 MB, less than 88.27% of Python3 online submissions for The K Weakest Rows in a Matrix.
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [r[1] for r in heapq.nsmallest(k,[[sum(g),i] for i,g in enumerate(mat)])]

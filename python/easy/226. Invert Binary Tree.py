"""
Given the root of a binary tree, invert the tree, and return its root.

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:

Input: root = [2,1,3]
Output: [2,3,1]

Example 3:

Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""


# My solutions
# Runtime: 38 ms, Beats 33.89%
# Memory Usage: 13.8 MB, Beats 94.98%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root



# Best solution (without recursion)
# Runtime: 33 ms, Beats 65.90%
# Memory Usage: 13.8 MB, Beats 94.98%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None

        bfs = deque([root])

        while bfs:
            node = bfs.popleft()
            node.left, node.right = node.right, node.left

            if node.left:
                bfs.append(node.left)
            if node.right:
                bfs.append(node.right)
                
        return root

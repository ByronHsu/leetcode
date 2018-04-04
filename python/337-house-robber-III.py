# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(now):
            if not now: return (0, 0)
            L, R = dfs(now.left), dfs(now.right)
            return (L[1] + R[1] + now.val, max(L[0], L[1]) + max(R[0], R[1])) # BLACK WHITE
        return max(dfs(root))

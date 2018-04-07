# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root):
        if root == None: return 0
        L, R = self.dfs(root.left) + 1, self.dfs(root.right) + 1
        self.ans = max(self.ans, L + R - 1)
        return max(L, R)
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        self.dfs(root)
        if not root: return 0 
        else: return self.ans - 1
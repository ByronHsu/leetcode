# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        def dfs(now):
            if now.left:
                dfs(now.left) 
            ans.append(now.val)
            if now.right:
                dfs(now.right)
        if root:
            dfs(root)
        return ans

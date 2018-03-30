# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        left, right = None, None
        if root == p or root == q: 
            return root
        if root.left: 
            left = self.lowestCommonAncestor(root.left, p, q)
        if root.right: 
            right = self.lowestCommonAncestor(root.right, p, q)
        if left and right: 
            return root 
        return left if left else right
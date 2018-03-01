# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def bidfs(l, r):
            if l == None and r == None:
                return True
            elif l and r and l.val == r.val:
                if not bidfs(l.left, r.right):
                    return False
                if not bidfs(l.right, r.left):
                    return False
                return True
            else:
                return False
        if root and not bidfs(root.left, root.right):
            return False:
        else:
            return True
        
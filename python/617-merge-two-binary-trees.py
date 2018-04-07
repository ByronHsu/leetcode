class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2: return None
        mNode = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
        mNode.left = self.mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
        mNode.right = self.mergeTrees(t1.right if t1 else None, t2.right if t2 else None)
        return mNode
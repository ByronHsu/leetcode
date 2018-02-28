# 設置一個index iterate preorder
# 每次去找到他在inorder的位置, 然後把inorder切成兩半下去遞迴

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        pos = {}
        for i, n in enumerate(inorder):
            pos[n] = i
        idx = 0
        def dfs(l, r):
            nonlocal idx
            cutval, idx = preorder[idx], idx+1
            cutidx = pos[cutval]
            T = TreeNode(cutval)
            if l <= cutidx-1:
                T.left = dfs(l, cutidx-1)
            if cutidx+1 <= r:
                T.right = dfs(cutidx+1, r)
            return T
        if len(inorder) > 0:
            return dfs(0, len(inorder)-1)
        else:
            return None
            

def test(L1, L2):
    Solution().buildTree(L1, L2)

if __name__ == '__main__':
    test([3,9,20,15,7], [9,3,15,20,7])
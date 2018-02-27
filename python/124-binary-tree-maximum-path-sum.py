def stringToTreeNode(inputValues):
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = -2**32
        def post(now):
            nonlocal ans
            lm, rm = -2**32, -2**32
            if now.left:
                lm = post(now.left)
            if now.right:
                rm = post(now.right)
            m1 = max(now.val, now.val+lm, now.val+rm)
            m2 = now.val+lm+rm
            ans = max(ans, m1, m2)
            return m1
        post(root)
        return ans

def test(L):
    Solution().maxPathSum(stringToTreeNode(L))

if __name__ == '__main__':
    test([-1,2,3,-3,4,5,-9,7,8])
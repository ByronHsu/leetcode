# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(now, gt = None, lt = None):
            print(now.val, gt, lt)
            # 走到這個點 先用gt, lt判斷是否合理
            if gt != None and not now.val > gt:
                return False
            if lt != None and not now.val < lt:
                return False
            # 繼續走下去
            if now.left and not check(now.left, gt, now.val):
                return False
            if now.right and not check(now.right, now.val, lt):
                return False

            return True

        if root and not check(root):
            return False

        return True

def test(L):
    print(Solution().isValidBST(stringToTreeNode(L)))

if __name__ == '__main__':
    # test([1,'null',1])
    # test([10,5,15,'null','null',6,20])
    test([0,'null',-1])
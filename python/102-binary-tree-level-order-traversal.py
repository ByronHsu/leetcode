from queue import Queue
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
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = Queue()
        L = []
        if root:
            q.put((0, root))
        while q.qsize() != 0:
            i, now = q.get()
            print(now.val)
            if len(L) <= i:
                L.append([now.val])
            else:
                L[i].append(now.val)
            if now.left:
                q.put((i+1, now.left))
            if now.right:
                q.put((i+1, now.right))

        print(L)
        return L
    
def test(L):
    Solution().levelOrder(stringToTreeNode(L))

if __name__ == '__main__':
    test([3,9,20,'null','null',15,7])
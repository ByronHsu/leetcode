class Node:
    def __init__(self, val):
        self.next = []
        self.val = val
        self.visit = False
        self.rec = False
    def addNext(self, i):
        self.next.append(i)
class Solution:
    def dfs(self, node, count):
        node.visit, node.rec = True, True
        for i in node.next:
            n = self.graph[i]
            if n.rec == True:
                return False
            if n.visit == False and self.dfs(n, count) == False:
                return False
        node.rec = False
        return True
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.graph = [Node(i) for i in range(numCourses)]
        for p in prerequisites:
            self.graph[p[1]].addNext(p[0])
        for i in range(numCourses):
            if self.graph[i].visit == False and self.dfs(self.graph[i], i) == False:
                return False
        return True
class Solution:
    def lowerBound(self, L, val):
        l, r = 0, len(L)-1
        while l < r:
            mid = (l+r) // 2
            if L[mid] < val:
                l = mid+1
            else:
                r = mid
        return l
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0: return False
        r1 = self.lowerBound([row[0] for row in matrix], target)
        r2 = r1-1
        c1, c2 = self.lowerBound(matrix[r1], target), self.lowerBound(matrix[r1-1], target)
        
        if  matrix[r1][c1] == target or matrix[r2][c2] == target:
            return True
        else:
            return False
        
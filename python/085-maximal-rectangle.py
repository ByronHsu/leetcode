class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        print(matrix)
        m, n = 0, 0
        m = len(matrix)
        if m > 0:
            n = len(matrix[0])

        for j in range(n):
            for i in range(m):
                matrix[i][j] = int(matrix[i][j])
                if i > 0 and matrix[i][j] != 0:
                    matrix[i][j] += matrix[i-1][j]
        ans = 0
        for l in matrix:
            ans = max(ans, self.largestRectangleArea(l))
        print(ans)
        return ans
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        heights.insert(0, 0)
        L = len(heights)
        ll = [0]*L
        stack = []
        for i in reversed(range(L)):
            while len(stack) and heights[i] < heights[stack[-1]]:
                ll[stack[-1]] = i
                stack.pop()
            stack.append(i)
        rr = [0]*L
        stack = []
        for i in range(L):
            while len(stack) and heights[i] < heights[stack[-1]]:
                rr[stack[-1]] = i
                stack.pop()
            stack.append(i)
        ans = 0
        for i in range(L):
            ans = max(ans, (rr[i]-ll[i]-1)*heights[i])
        return ans


if __name__ == '__main__':
    print(Solution().maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
    print(Solution().maximalRectangle([]))
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
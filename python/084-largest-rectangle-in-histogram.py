class Solution:
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
    print(Solution().largestRectangleArea([2,1,5,6,2,3]))

# 0 2 1 5 6 2 3 0
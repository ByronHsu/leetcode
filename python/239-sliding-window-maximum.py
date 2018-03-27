import collections
# 使用deque
# 保持deque中為遞減的
class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []
        d = collections.deque()
        for i in range(len(nums)):
            while d and nums[d[-1]] < nums[i]:
                d.pop()
            d.append(i)
            if d[0] < i-k+1:
                d.popleft()
            if i >= k-1:
                ans.append(nums[d[0]])
        return ans

if __name__ == '__main__':
    Solution().maxSlidingWindow([7,2,4],2)
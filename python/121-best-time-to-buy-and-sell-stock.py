class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m, M = 0, 0
        ans = 0
        for i in range(len(prices)):
            if prices[i] <= prices[m]:
                m, M = i, i
            else:
                M = i
            ans = max(ans, prices[M]-prices[m])
        return ans
        
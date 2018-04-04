class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        count = [0] * (num + 1)
        for i in range(1, num + 1):
            count[i] = count[i >> 1] + (i & 1)
        return count[: num + 1]
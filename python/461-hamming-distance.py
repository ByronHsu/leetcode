class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x ^ y
        count = 0
        while z != 0:
            if z % 2 == 1: count += 1
            z = z // 2
        return count
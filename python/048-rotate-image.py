import math
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        M = len(matrix)
        for i in range(M):
            for j in range(i, M):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # print(matrix)
        for i in range(math.floor(M/2)):
            for j in range(M):
                matrix[j][i], matrix[j][M-i-1] = matrix[j][M-i-1], matrix[j][i]
        # print(matrix)
        # return matrix

def test(M):
    print(Solution().rotate(M))

if __name__ == '__main__':
    test([
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
])
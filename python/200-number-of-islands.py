class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        R, C = [-1, 1, 0, 0], [0, 0, 1, -1]
        m, n = len(grid), len(grid[0])
        def dfs(r, c):
            grid[r][c] = '2' # visited
            for i in range(4):
                nr, nc = r + R[i], c + C[i]
                if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and grid[nr][nc] == '1':
                    dfs(nr, nc)
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    ans += 1
        return ans

if __name__ == '__main__':
    Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
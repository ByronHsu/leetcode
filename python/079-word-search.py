class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board) + 2
        n = len(board[0]) + 2
        board.insert(0, ['#']*n)
        for i in range(1, m-1):
            board[i].append('#')
            board[i].insert(0, '#')
        board.append(['#']*n)
        visited = [[False for i in range(n)]for j in range(m)]
        r = [1,-1,0,0]
        c = [0,0,1,-1]
        def dfs(index, i, j):
            if index >= len(word):
                return True
            if board[i][j] == word[index]:
                for k in range(4):
                    if not visited[i+r[k]][j+c[k]]:
                        visited[i+r[k]][j+c[k]] = True
                        if dfs(index+1, i+r[k], j+c[k]):
                            return True
                        visited[i+r[k]][j+c[k]] = False
            return False

        for i in range(1, m-1):
            for j in range(1, n-1):
                visited[i][j] = True
                if dfs(0, i, j):
                    return True
                visited[i][j] = False
        return False

if __name__ == '__main__':
    print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
"ABCCED"))
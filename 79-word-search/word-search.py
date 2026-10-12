class Solution(object):
    def exist(self, board, word):
        n = len(board)
        m = len(board[0])

        def dfs(i, j, c):
            if c == len(word):
                return True

            if i < 0 or i >= n or j < 0 or j >= m:
                return False

            if board[i][j] != word[c]:
                return False

            a = board[i][j]
            board[i][j] = "#"

            if (dfs(i + 1, j, c + 1) or
                dfs(i - 1, j, c + 1) or
                dfs(i, j + 1, c + 1) or
                dfs(i, j - 1, c + 1)):
                return True

            board[i][j] = a
            return False

        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0):
                    return True

        return False
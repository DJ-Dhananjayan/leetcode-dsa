class Solution:
    def getMaximumGold(self, g: List[List[int]]) -> int:
        ans = 0
        m, n = len(g), len(g[0])
        visited = set()
        def bt(i: int, j: int, s: int):
            nonlocal ans
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if g[i][j] == 0 or (i, j) in visited:
                return
            visited.add((i, j))
            s += g[i][j]
            ans = max(ans, s)
            bt(i - 1, j, s)
            bt(i + 1, j, s)
            bt(i, j - 1, s)
            bt(i, j + 1, s)
            visited.remove((i, j))
        for i in range(m):
            for j in range(n):
                if g[i][j] != 0:
                    bt(i, j, 0)
        return ans
from collections import deque
class Solution:
    def bfs(self,r,c,visited,grid):
        n = len(grid)
        m = len(grid[0])
        q = deque([(r,c)])
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        while q:
            r,c = q.popleft()
            for dr,dc in directions:
                nr = r + dr
                nc = c + dc
                if 0<=nr<n and 0<=nc<m and not visited[nr][nc] and grid[nr][nc]=='1':
                    visited[nr][nc] = 1
                    q.append((nr,nc))
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[0]*m for _  in range(n)]
        count = 0
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j]=='1':
                    count += 1
                    self.bfs(i,j,visited,grid)
        return count
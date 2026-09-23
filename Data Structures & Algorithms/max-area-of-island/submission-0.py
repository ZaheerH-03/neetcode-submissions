from collections import deque
class Solution:
    def bfs(self,r,c,visited,grid):
        n = len(grid)
        m = len(grid[0])
        q = deque([(r,c)])
        visited[r][c] = 1
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        area = 0
        while q:
            row,col = q.popleft()
            area += 1
            for dr,dc in directions:
                nr = row + dr
                nc = col + dc
                if 0<=nr<n and 0<=nc<m and not visited[nr][nc] and grid[nr][nc]==1:
                    visited[nr][nc]=1
                    q.append((nr,nc))
        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[0]*m for _ in range(n)]
        max_area = 0
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j]==1:
                    area = self.bfs(i,j,visited,grid)
                    max_area = max(max_area,area)
        return max_area
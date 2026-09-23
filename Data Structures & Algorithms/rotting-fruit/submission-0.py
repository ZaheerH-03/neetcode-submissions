from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        q = deque()
        fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append([i,j])
                elif grid[i][j]==1:
                    fresh += 1
        
        if fresh == 0:
            return 0
            
        min = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0<=nr<n and 0<=nc<m and grid[nr][nc]==1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append([nr,nc])
            min +=1

        if fresh == 0:
            return min 
        else:
            return -1


from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n,m = len(grid),len(grid[0])
        visit = set()
        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    q.append([i,j])
                    visit.add((i,j))
        dist = 0
        def addRoom(r,c):
            if (r<0 or r==n or c < 0 or c==m or (r,c) in visit or grid[r][c]==-1):
                return
            visit.add((r,c))
            q.append([r,c])
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                addRoom(r+1,c)
                addRoom(r-1,c)
                addRoom(r,c+1)
                addRoom(r,c-1)
            dist += 1

        
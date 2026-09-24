from collections import defaultdict , deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0]*numCourses
        for u,v in prerequisites:
            graph[v].append(u)
            in_degree[u] += 1
        
        q = deque([])
        topo = []
        for i in range(numCourses):
            if in_degree[i]==0:
                q.append(i)

        while q:
            u = q.popleft()
            topo.append(u)
            for v in graph[u]:
                in_degree[v] -= 1
                if in_degree[v]==0:
                    q.append(v)
        if len(topo)==numCourses:
            return topo
        else:
            return []
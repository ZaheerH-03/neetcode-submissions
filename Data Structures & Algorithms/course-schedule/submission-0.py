from collections import defaultdict ,deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
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
            for pre in graph[u]:
                in_degree[pre] -= 1
                if in_degree[pre] == 0:
                    q.append(pre)
        if len(topo)==numCourses:
            return True
        else:
            return False


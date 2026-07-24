class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {i: [] for i in range(numCourses)}
        visited = set()

        for c, p in prerequisites:
            graph[c].append(p)
        
        def dfs(c):
            if c in visited: return False

            visited.add(c)
            
            for pre in graph[c]:
                if not dfs(pre):
                    return False
            visited.remove(c)
            graph[c] = []
            return True

        for c in range(numCourses):
            if not dfs(c): return False
        return True
        
        
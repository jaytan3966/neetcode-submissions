class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        visited, seen = set(), set()
        ans = []
        
        for c, p in prerequisites:
            graph[c].append(p)
        
        def dfs(c):
            if c in visited: return False

            visited.add(c)
            
            for pre in graph[c]:
                if not dfs(pre):
                    return False
            visited.remove(c)

            if c not in seen: 
                ans.append(c)
                seen.add(c)
            graph[c] = []
            return True

        for c in range(numCourses):
            if not dfs(c): return []
        return ans
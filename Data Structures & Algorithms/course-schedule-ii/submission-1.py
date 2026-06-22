class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj =  { c:[] for c in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)

        visited = set()
        cycle = set()

        output = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for pre in adj[crs]:
                if not dfs(pre): return False
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return output


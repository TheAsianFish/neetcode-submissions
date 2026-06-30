class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not n:
            return 0
        
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()

        def dfs(i):
            visited.add(i)
            for j in adj[i]:
                if j not in visited:
                    dfs(j)

        output = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                output += 1
        
        return output

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #find all rotten fruits
        # run BFS and keep track of time
        # when queue is empty, do O(n*m) to find any fresh fruit remainging
        # either keep track of visited set, or check if it is 2 (rotten) or empty cell and return
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append([i, j])
                    visited.add((i, j))
        
        if not queue:
            for i in range(ROWS):
                for j in range(COLS):
                    if grid[i][j] == 1:
                        return -1
            return 0
        
        def addCell(i, j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or (i, j) in visited or grid[i][j] == 0:
                return
            visited.add((i,j))
            queue.append([i,j])
            grid[i][j] = 2

        time = -1
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                addCell(i + 1, j)
                addCell(i - 1, j)
                addCell(i, j + 1)
                addCell(i, j - 1)
            time += 1
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return -1

        return time 




            
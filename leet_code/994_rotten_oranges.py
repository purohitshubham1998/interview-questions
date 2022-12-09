"""Example 1"""
# grid = [
#     [2,1,1],
#     [1,1,0],
#     [0,1,1]
# ]
"""Example 2"""
grid = [
    [0,1,2],
    [0,1,2],
    [2,1,1]
]

def rotten_oranges(grid):
    queue = []
    visited = []
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        visited.append([False]*(cols))
        for j in range(cols):
            if grid[i][j] == 2:
                queue.append((i, j, 0))

    def bfs(grid, visited, queue):
        time_counter = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while len(queue) != 0:
            currentRow, currentCol, currentTime = queue.pop(0)
            if visited[currentRow][currentCol]:
                continue
            time_counter = max(time_counter, currentTime)
            visited[currentRow][currentCol] = True
            for dr, dc in directions:
                newRow = dr + currentRow
                newCol = dc + currentCol
                if newRow in range(rows) and newCol in range(cols) and grid[newRow][newCol] not in [0, 2]:
                    grid[newRow][newCol] = 2
                    queue.append((newRow, newCol, currentTime+1))
        return time_counter
    result = bfs(grid, visited, queue)
    return result

result = rotten_oranges(grid)
print(result)
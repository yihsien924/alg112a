#使用ChatGPY完成並理解
def solve_maze(maze):
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0

    def dfs(x, y):
        if x == rows - 1 and y == cols - 1:
            result.append(path[:])  #考慮到達終點的情況
            return
        for direction in directions:
            new_x, new_y = x + direction[0], y + direction[1]
            if is_valid(new_x, new_y) and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                path.append((new_x, new_y))
                dfs(new_x, new_y)
                path.pop()
                visited[new_x][new_y] = False

    if not maze or not maze[0]:
        return []

    rows, cols = len(maze), len(maze[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  #上、下、左、右
    visited = [[False] * cols for _ in range(rows)]
    result = []
    path = [(0, 0)]  #起點

    visited[0][0] = True
    dfs(0, 0)

    return result

#範例迷宮
maze = [
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0]
]

solutions = solve_maze(maze)
for solution in solutions:
    print(solution)
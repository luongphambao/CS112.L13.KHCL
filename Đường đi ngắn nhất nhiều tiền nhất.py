def MaximumPath(maze,N,M):
    sum = [[0 for i in range(M + 1)]
           for i in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, M + 1):

            sum[i][j] = (max(sum[i - 1][j],
                             sum[i][j - 1]) +
                         maze[i - 1][j - 1])
    return sum[N][M]
r, c = [int(i) for i in input().split()]
maze = []
for i in range(r):
    maze.append([int(i) for i in input().split()])
print(MaximumPath(maze,r,c))
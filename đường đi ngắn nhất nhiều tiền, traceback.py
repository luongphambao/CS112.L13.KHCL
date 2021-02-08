def shortest_max_pathbu(maze, r, c):
    
    for i in range(r-1, -1, -1):
        for j in range(c-1, -1, -1):
            nr = i + 1
            nc = j + 1
            tmp1 = 0
            tmp2 = 0
            if nr < r:
                tmp1 = maze[nr][j]
            if nc < c:
                tmp2 = maze[i][nc]
            
            maze[i][j] = maze[i][j] + max(tmp1, tmp2)
    
    i = 0
    print(maze[0][0])
    j = 0
    path = [[0,0]]
    while i+1<r and j+1 < c:
        if maze[i][j+1] >= maze[i+1][j]:
            path.append([i, j+1])
            j+=1
        else:
            path.append([i+1, j])
            i+=1
    if j+1< c and [i, j+1] not in path :
        while j+1 < c:
            path.append([i,j+1])
            j+=1
    if i+1 < r and [i+1,j] not in path:
        while i+1 < r:
            path.append([i+1, j])
            i+=1
    if [r-1, c-1] not in path:
        path.append([r-1, c-1])
    for i in range(len(path)-1, -1, -1):
        print(*path[i])
    return
r, c = [int(i) for i in input().split()]
maze = []
for i in range(r):
    maze.append([int(i) for i in input().split()])
memoi = [[0 for i in range(c)] for j in range(r)]

(shortest_max_pathbu(maze, r, c))
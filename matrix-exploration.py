from collections import deque

def bfs(matrix, specials, N, M):
    distance = [[float('inf')] * M for _ in range(N)]
    queue = deque()

    for x, y in specials:
        queue.append((x, y))
        distance[x][y] = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == '.' and distance[nx][ny] == float('inf'):
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))
    
    total_distance = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == '.':
                total_distance += distance[i][j]

    return total_distance

N, M, K = map(int, input().split())
matrix = [list(input().strip()) for _ in range(N)]
specials = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(K)]

print(bfs(matrix, specials, N, M))

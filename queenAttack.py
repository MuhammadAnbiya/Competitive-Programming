n = 5
r_q = 4
c_q = 3

# matrix = [[float('inf')] * n for _ in range(n)]
# matrix[row][col] = 'Queen'
obstacles = [(5,5),(2,3),(4,2)]
# for x, y in obstacles:
#     matrix[x][y] = 'Ob'

# print(matrix)


matrix = [[float('inf')] * n for _ in range(n)]
# queue = deque()

matrix[n-r_q][c_q-1] = 'Q'

for x, y in obstacles:
    matrix[n-x][y-1] = 'Ob'

# directions = [(-1,0)]#,(1,0),(0,1),(0,-1),(-1,1),(-1,-1),(1,-1),(1,1)]

# for x, y in directions:
#     nx, ny = r_q + x, c_q + y
# print(nx, ny)
    
print(matrix)

attU = 0
attD = 0
attL = 0
attR = 0
attRU = 0
attLU = 0
attRD = 0
attLD = 0


x = n-r_q #1
y = c_q -1 #2
nx = x
ny = y


# while x > -1 or x < n or y > -1 or y < n 


# while nx-1 > -1:
    # if matrix[x][y] != 'Ob':
        # attU += 1
    # nx -= 1
# print(attU)
# print(x)

# while y < n-1:
    # attR += 1
    # y += 1

# while y > -1:
    # attL += 1
    # y -= 1

# print(attR)
# print(attL)



# while nx > -1 or nx < n or ny > -1 or ny < n:
#     if matrix[x-1][y] != 'Ob':
#         attU += 1
#         nx -= 1
#     if matrix[x+1][y] != 'Ob':
#         attD += 1 
#         nx += 1
#     if matrix[x-1][y] != 'Ob':
#         attR += 1 
#         nx -= 1
#     if matrix[x-1][y] != 'Ob':
#         attD += 1 
#         nx -= 1

# attTotal = attU + attD + attR + attL + attRU + attLU + attRD + attLD
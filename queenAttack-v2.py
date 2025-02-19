n = 5
r_q = 4
c_q = 3

obstacles = [(5,5),(2,3),(4,2)]

matrix = [[float('inf')] * n for _ in range(n)]
matrix[n - r_q][c_q - 1] = 'Q'

for x, y in obstacles:
    matrix[n - x][y - 1] = 'Ob'

directions = [
    (-1, 0),  # atas
    (1, 0),   # bawah
    (0, -1),  # kiri
    (0, 1),   # kanan
    (-1, -1), # kiri atas
    (-1, 1),  # kanan atas
    (1, -1),  # kiri bawah
    (1, 1)    # kanan bawah
]

total_moves = 0
for d in directions:
    x, y = n - r_q, c_q - 1  
    print(d[1])
    print("test")
    while True:
        
        x += d[0]
        y += d[1]
    
        print(x)
        print(y)
        print(d)
        if x < 0 or x >= n or y < 0 or y >= n:
            break
        
        if matrix[x][y] == 'Ob':
            break
        
        total_moves += 1
print(total_moves)
def count_zero_parts(matrix):
    if not matrix:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]

    def dfs(r, c):
        # Cek batasan dan jika sudah dikunjungi atau bukan 0
        if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c] or matrix[r][c] == 1:
            return
        visited[r][c] = True
        # Cek tetangga
        dfs(r + 1, c)  # Bawah
        dfs(r - 1, c)  # Atas
        dfs(r, c + 1)  # Kanan
        dfs(r, c - 1)  # Kiri

    part_count = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0 and not visited[i][j]:
                dfs(i, j)  # Mulai DFS untuk bagian baru
                part_count += 1

    return part_count

# Array dua dimensi
matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
]

# Menghitung jumlah bagian kosong (0)
result = count_zero_parts(matrix)
print("Jumlah bagian terpisah dari angka 0:", result)

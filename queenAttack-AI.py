def queensAttack(n, k, r_q, c_q, obstacles):
    # r_q = 4
    # c_q = 3
    # n = 5


    # Initial maximum distances in each direction
    top = n - r_q   # 5 - 4 = 1 

    bottom = r_q - 1    # 4 -1 = 3
    right = n - c_q     # 5 - 3 = 2 
    left = c_q - 1  # 3 - 1 = 2 
    top_left = min(top, left)   # 1, 2 = 1
    top_right = min(top, right) # 1, 2 = 1
    bottom_left = min(bottom, left) # 3, 2 = 2
    bottom_right = min(bottom, right) # 3, 2 = 2

    # Process obstacles to reduce the movement range
    for r_o, c_o in obstacles:
        if c_o == c_q:  # Same column
            if r_o > r_q: # 
                top = min(top, r_o - r_q - 1)
            else:
                bottom = min(bottom, r_q - r_o - 1)
        elif r_o == r_q:  # Same row
            if c_o > c_q:
                right = min(right, c_o - c_q - 1)   
            else:
                left = min(left, c_q - c_o - 1)
        elif abs(r_o - r_q) == abs(c_o - c_q):  # Diagonal
            if r_o > r_q and c_o > c_q:  # Top right diagonal
                top_right = min(top_right, r_o - r_q - 1)
            elif r_o > r_q and c_o < c_q:  # Top left diagonal
                top_left = min(top_left, r_o - r_q - 1)
            elif r_o < r_q and c_o > c_q:  # Bottom right diagonal
                bottom_right = min(bottom_right, r_q - r_o - 1)
            elif r_o < r_q and c_o < c_q:  # Bottom left diagonal
                bottom_left = min(bottom_left, r_q - r_o - 1)

    # Total possible moves
    total_moves = top + bottom + right + left + top_left + top_right + bottom_left + bottom_right

    return total_moves

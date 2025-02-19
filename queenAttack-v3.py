def queensAttack(n, k, r_q, c_q, obstacles):
    t = n - r_q
    b = r_q - 1
    r = n - c_q
    l = c_q - 1
    tr = min(t, r)
    tl = min(t, l)
    br = min(b, r)
    bl = min(b, l)
    
    for r_o, c_o in obstacles:
        if c_o == c_q:
            if r_o > r_q:
                t = min(t, r_o - r_q - 1)
            else:
                b = min(b, r_q - r_o - 1)
        elif r_o == r_q:
            if c_o > c_q:
                r = min(r, c_o - c_q - 1)
            else:
                l = min(l, c_q - c_o - 1)
        elif abs(r_o - r_q) == abs(c_o - c_q):
            if r_o > r_q and c_o > c_q:
                tr = min(tr, r_o - r_q - 1)
            elif r_o > r_q and c_o < c_q:
                tl = min(tl, r_o - r_q - 1)
            elif r_o < r_q and c_o > c_q:
                br = min(br, r_q - r_o - 1)
            elif r_o < r_q and c_o < c_q:
                bl = min(bl, r_q - r_o - 1)
    total = t + b + r + l + tr + tl + br + bl
    return total

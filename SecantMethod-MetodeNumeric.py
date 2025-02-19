def secant_method(f, x0, x1, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)
        
        if f_x1 - f_x0 == 0:
            return None
        
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        
        if abs(x2 - x1) < tol:
            return x2
        
        x0, x1 = x1, x2
    
    return None

result = secant_method(lambda x: x**2 - 4, 1, 3)
print("Akar yang ditemukan:", result)

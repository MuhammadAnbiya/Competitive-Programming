def f(x):
    return 4*x**3 - 6*x**2 + 7*x - 2

def bisection(a, b, tol, max_iter=1000):
    if f(a) * f(b) > 0:
        print("no root")
        return None
    
    iteration = 0
    
    while (abs(b - a) >= tol and iteration < max_iter):
        c = (a + b) / 2
        fc = f(c)
        
        if abs(fc) < tol:
            return c
        
        if f(a) * fc < 0:
            b = c
        else:
            a = c
            
        iteration += 1
    return (a + b) / 2, iteration

a = 0  
b = 5
toleransi = 0.001 
max_iterasi = 100  

akar, iteration = bisection(a, b, toleransi, max_iterasi)

if akar is not None:
    print(f"\nAkar yang ditemukan: {akar:.6f}")
    print(f"Nilai f(x) pada akar: {f(akar):.6f}")
    print(f"Maka perubahan suhu mencapai 0 derajat Celcius pada waktu sekitar : {akar:.3f} jam, pada iterasi ke-{iteration}")

    
def isPrime1(start, end):
    prime = []
    for num in range(max(2,start), end+1):
        is_Prime=True
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                is_Prime = False
                break
        if is_Prime:
            prime.append(num)
    return prime

def isPrime2(start, end):
    primes = []
    for num in range(max(2, start), end+1):
        is_prime = True
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

s = int(input("awal"))
e = int(input("akhir"))
result = isPrime1(s,e)
print(result)

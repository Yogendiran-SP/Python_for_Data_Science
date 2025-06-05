def is_prime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return 0
    return n
result = 0
for i in range(2,2000000):
    print(is_prime(i),end=", ")
    result+=is_prime(i)
print("Sum of all prime numbers below 2 Million:", result)
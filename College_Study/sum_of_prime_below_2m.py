from tqdm import tqdm

def is_prime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return 0
    return n
result = 0

# tqdm progress bar added
for i in tqdm(range(2,2000000),desc="Checking primes",ncols=100):  
    result+=is_prime(i)
print("Sum of all prime numbers below 2 Million:", result)
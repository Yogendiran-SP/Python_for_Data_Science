def gcd(a,b):
    if b<a:
        a,b=b,a
    for i in range(a,0,-1):
        if a%i==0 and b%i==0:
            return i

a,b = map(int,input("Enter the numbers: ").split())
print(f"GCD of {a} and {b} is {gcd(a,b)}")
print(f"LCM of {a} and {b} is {a*b/gcd(a,b)}")
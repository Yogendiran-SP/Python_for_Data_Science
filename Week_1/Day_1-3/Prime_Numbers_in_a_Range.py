def checking_prime_or_not(n):
    for i in range(2,n//2):
        if(n/i==0):
            return n,"is not a Prime Number"
    else:
        return n,"is a Prime Number" 

if __name__=="__main__":
    print("PRIME NUMBERS IN A RANGE\n________________________\n")
    print("1. Checking Prime or not\n2. Printing Prime Numbers within n\n3. Printing n Prime Numbers\n4. Sum of n Prime numbers\n5. ")
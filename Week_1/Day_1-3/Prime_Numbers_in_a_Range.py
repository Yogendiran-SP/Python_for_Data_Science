def is_prime(n):
    if n>1:
        for i in range(2,(n//2)+1):
            if(n%i==0):
                return False
        else:
            return True
    else:
        return False

def within_n(n):
    for i in range(1,n+1):
        if is_prime(i):
            print(i,end=" ")

def n_prime_numbers(n):
    i=1
    var=1
    while (i<=n):
        if is_prime(var):
            print(var,end=" ")
            i+=1
        var+=1

def sum_within_n(n):
    sum=0
    for i in range(1,n+1):
        if is_prime(i):
            sum+=i
    return sum

def sum_of_n_prime_numbers(n):
    sum=0
    i=1
    var=1
    while (i<=n):
        if is_prime(var):
            i+=1
            sum+=var
        var+=1
    return sum

if __name__=="__main__":

    while True:
        print("PRIME NUMBERS IN A RANGE\n________________________\n")
        print("1. Checking Prime or not\n2. Printing Prime Numbers within n\n3. Printing n Prime Numbers\n4. Sum of Prime numbers within n\n5. Sum of n Prime Numbers")

        choice=int(input("Enter your choice: "))

        if choice==1:
            try:
                n=int(input("Enter the value of n: "))
                res=n,"is a Prime Number" if is_prime(n) else "is not an Prime Number"
                print(*res,"\n________________________\n")

            except:
                print("Invalid input")

        elif choice==2:
            try:
                n=int(input("Enter the value of n: "))
                within_n(n)
                print("\n________________________\n")
            except:
                print("Invalid input")

        elif choice==3:
            try:
                n=int(input("Enter the value of n: "))
                n_prime_numbers(n)
                print("\n________________________\n")
            except:
                print("Invalid input")

        elif choice==4:
            try:
                n=int(input("Enter the value of n: "))
                print(sum_within_n(n),"\n________________________\n")
            except:
                print("Invalid input")

        elif choice==5:
            try:
                n=int(input("Enter the value of n: "))
                print(sum_of_n_prime_numbers(n),"\n________________________\n")
            except:
                print("Invalid input")
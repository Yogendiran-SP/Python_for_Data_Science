def without_using_recursion(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f

def using_recursion(n):
    if n==1 or n==0:
        return 1
    else:
        return n*using_recursion(n-1)

if __name__=="__main__":
    while True:
        print("FACTORIAL USING / WITHOUT USING RECURSION\n_________________________________________\n")
        print("1. Without using Recursion\n2. Using Recursion\n")
        choice=int(input("Enter your choice: "))

        if choice==1:
            try:
                n=int(input("Enter the value of n: "))
                if n>0:
                    print("\nFactorial of",n,"is",without_using_recursion(n),"\n_________________________________________\n")
                else:
                    print("\nFactorial is not possible for non-positive numbers","\n_________________________________________\n")
            except:
                print("Invalid input")

        elif choice==2:
            try:
                if n>0:
                    n=int(input("Enter the value of n: "))
                    print("\nThe Factorial of",n,"is",using_recursion(n),"\n_________________________________________\n")
                else:
                    print("\nFactorial is not possible for non-positive numbers","\n_________________________________________\n")
            except:
                print("Invalid input")
        
        else:
            print("Inavlid choice")
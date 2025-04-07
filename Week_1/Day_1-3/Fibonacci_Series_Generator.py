def within_n(n):
    a,b=0,1
    print(a,b,end=" ")
    while((a+b)<=n):
        print(a+b,end=" ")
        a,b=b,a+b

def upto_n(n):
    a,b,i=0,1,3
    print(a,b,end=" ")
    while(i<=n):
        print(a+b,end=" ")
        a,b=b,a+b
        i+=1

def sum_within_n(n):
    a,b=0,1
    s=(a+b)
    while True:
        s+=(a+b)
        if s>n:
            s-=(a+b)
            break
        a,b=b,a+b
    return s

def sum_of_n_terms(n):
    a,b=0,1
    s=(a+b)
    for i in range(3,n+1):
        s+=(a+b)
        a,b=b,(a+b)
    return s

if __name__=="__main__":
    while True:
        print("FIBONACCI SERIES GENERATOR\n__________________________\n")
        print("1. Fibonacci Series within n\n2. Fibonacci Series upto n terms\n3. Sum of the Fibonacci Series within n\n4. Sum of Fibonacci Series of n terms")
        choice=int(input("Enter your choice (1 or 2 or 3 or 4): "))
        if choice==1:
            try:
                n=int(input("Enter the value of n: "))
                print("")
                within_n(n)
                print("\n__________________________\n")
            except:
                print("Invalid input")

        elif choice==2:
            try:
                n=int(input("Enter the value of n: "))
                print("")
                upto_n(n)
                print("\n__________________________\n")
            except:
                print("Invalid input")

        elif choice==3:
            try:
                n=int(input("Enter the value of n: "))
                print("\n",sum_within_n(n),"\n__________________________\n")

            except:
                print("Invalid input")

        elif choice==4:
            try:
                n=int(input("Enter the value of n: "))
                print("\n",sum_of_n_terms(n),"\n__________________________\n")

            except:
                print("Invalid input")

        else:
            print("Invalid choice")
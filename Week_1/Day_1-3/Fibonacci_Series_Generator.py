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

def sum_of_n(n):
    a,b,s=0,1,0
    print(a,b,end=" ")
    while(s<=n):
        print(a+b,end=" ")
        a,b=b,a+b
        s+=(a+b)

if __name__=="__main__":

    print("1. Fibonacci Series within n\n2. Fibonacci Series upto n terms\n3. Sum of the Fibonacci Series within n")
    choice=int(input("Enter your choice (1 or 2 or 3): "))
    if choice==1:
        try:
            n=int(input("Enter the value of n: "))
            within_n(n)
        except:
            print("Invalid input")

    elif choice==2:
        try:
            n=int(input("Enter the value of n: "))
            upto_n(n)
        except:
            print("Invalid input")

    elif choice==3:
        try:
            n=int(input("Enter the value of n: "))
            sum_of_n(n)
        except:
            print("Invalid input")
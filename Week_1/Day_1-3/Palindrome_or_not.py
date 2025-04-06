def getting_as_str(a):
    res = a, "is an Armstrong Number" if a==a[::-1] else "is not an Armstrong Number"
    return res

def converting_int_to_str(a):
    a=str(a)
    res = a, "is an Armstrong Number" if a==a[::-1] else "is not an Armstrong Number"
    return res

def getting_as_int(a):
    copy=a
    i,res=1,0
    while(a>0):
        res+=(a%10)*i
        a=a//10
        i*=10
    result = copy, "is an Armstrong Number" if copy==res else "is not an Armstrong Number"
    return result

if __name__=="__main__":
    while True:
        print("CHECKING WHETHER A NUMBER IS PALINDROME OR NOT\n_____________________________________________\n")
        print("1. Getting input as a itself\n2. Converting integer input to string\n3. Geeting input as a integer")
        choice=int(input("Enter your choice (1 or 2 or 3): "))
        if choice==1:
            try:
                a=input("Enter the number: ")
                print(*getting_as_str(a),"\n_____________________________________________\n")
            except:
                print("invalid input")
        elif choice==2:
            try:
                a=int(input("Enter the number: "))
                print(*converting_to_str(a),"\n_____________________________________________\n")
            except:
                print("Invalid input")
        elif choice==3:
            try:
                a=int(input("Enter the number: "))
                print(*getting_as_int(a),"\n_____________________________________________\n")
            except:
                print("Invalid input")
        else:
            print("Invalid Choice")
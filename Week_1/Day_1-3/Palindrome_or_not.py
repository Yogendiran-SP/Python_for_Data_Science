def getting_as_str(a):
    res = a, "is an Palindrome" if a==a[::-1] else "is not an Palindrome"
    return res

def converting_int_to_str(a):
    a=str(a)
    res = a, "is an Palindrome" if a==a[::-1] else "is not an Palindrome"
    return res

def getting_as_int(a):
    copy=a
    i,res=1,0
    while(a>0):
        res+=(a%10)*i
        a=a//10
        i*=10
    result = copy, "is an Palindrome" if copy==res else "is not an Palindrome"
    return result

if __name__=="__main__":
    while True:
        print("CHECKING WHETHER A NUMBER IS PALINDROME OR NOT\n_____________________________________________\n")
        print("1. Getting input as a string itself\n2. Converting integer input to string\n3. Geeting input as a integer")
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
                print(*converting_int_to_str(a),"\n_____________________________________________\n")
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
def getting_as_str(a):
    return a, "is a Palindrome" if a==a[::-1] else "is not a Palindrome"

def converting_int_to_str(a):
    a=str(a)
    return a, "is a Palindrome" if a==a[::-1] else "is not a Palindrome"

def converting_str_to_int(a):
    a=int(a)
    copy=a
    res=0
    while(a>0):
        res=res*10+a%10
        a//=10
    result = copy, "is a Palindrome" if copy==res else "is not a Palindrome"
    return result

def getting_as_int(a):
    copy=a
    res=0
    while(a>0):
        res=res*10+(a%10)
        a=a//10
    return copy, "is a Palindrome" if copy==res else "is not a Palindrome"

if __name__=="__main__":
    while True:
        print("CHECKING WHETHER A NUMBER IS PALINDROME OR NOT\n_____________________________________________\n")
        print("1. Getting input as a string itself\n2. Converting integer input to string\n3. Converting string input to integer\n4. Getting input as a integer")
        choice=int(input("Enter your choice (1 or 2 or 3 or 4): "))
        if choice==1:
            try:
                a=input("Enter a string: ")
                print(*getting_as_str(a),"\n_____________________________________________\n")
            except:
                print("invalid input")
        elif choice==2:
            try:
                a=int(input("Enter a number: "))
                print(*converting_int_to_str(a),"\n_____________________________________________\n")
            except:
                print("Invalid input")
        elif choice==3:
            try:
                a=input("Enter a number: ")
                print(*converting_str_to_int(a),"\n_____________________________________________\n")
            except:
                print("Invalid input")
        elif choice==4:
            try:
                a=int(input("Enter a number: "))
                print(*getting_as_int(a),"\n_____________________________________________\n")
            except:
                print("Invalid input")
        else:
            print("Invalid Choice")
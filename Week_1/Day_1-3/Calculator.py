def evalcalc(a):
    return eval(a)

def opcalc(a,b,c):
    if b=='+':return a+c
    elif b=='-':return a-c
    elif b=='/':return a/c
    elif b=='//':return a//c
    elif b=='%':return a%c
    elif b=='*':return a*c
    elif b=='^' or b=='**':return a**c

if __name__=="__main__":
    while True:
        print("1. Calculate using Eval function\n2. Calculate using operators & operands")
        choice=int(input("Enter your choice (1 or 2): "))

        if choice==1:
            try:
                print("Result: ",evalcalc(input("Enter the calculation: ")))
            except:
                print("Invalid input")
        elif choice==2:
            try:
                a=int(input("Enter the first operand: "))
                b=input("Enter the operator: ")
                c=int(input("Enter the second operand: "))
                print("Result: ",opcalc(a,b,c))
            except:
                print("Invalid input")
        else:
            print("Invalid choice")
def evalcalc(a):
    return eval(a)

def opcalc(a,b,c):
    operations={
        '+':lambda  a,b:a+b,
        '-':lambda a,b:a-b,
        '/':lambda a,b:a/b,
        '%':lambda a,b:a%b,
        '//':lambda a,b:a//b,
        '*':lambda a,b:a*b,
        '^':lambda a,b:a**b,
        '**':lambda a,b:a**b,
    }
    return operations[b](a,c)

if __name__=="__main__":
    while True:
        print("CALCULATOR\n__________\n")
        print("1. Calculate using Eval function\n2. Calculate using operators & operands")
        choice=int(input("Enter your choice (1 or 2): "))

        if choice==1:
            try:
                print("\nResult: ",evalcalc(input("Enter the calculation: ")),"\n__________\n")
            except:
                print("Invalid input")
        elif choice==2:
            try:
                a=int(input("Enter the first operand: "))
                b=input("Enter the operator: ")
                c=int(input("Enter the second operand: "))
                print("\nResult: ",opcalc(a,b,c),"\n__________\n")
            except:
                print("Invalid input")
        else:
            print("Invalid choice")
def checking(a):
    copy,res = a,0
    while(a>0):
        res += (a%10)**len(str(copy))
        a = a//10
    result = copy, "is an Armstrong Number" if copy==res else "is not an Armstrong Number"
    return result

if __name__=="__main__":
    while True:
        print("\nCHECKING WHETHER A NUMBER IS ARMSTRONG OR NOT\n_____________________________________________\n")
        a=int(input("Enter the number: "))
        print(*checking(a),"\n_____________________________________________\n")
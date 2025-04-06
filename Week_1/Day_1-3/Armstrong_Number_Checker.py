def checking(a):
    copy,res = a,0
    while(a>0):
        res += (a%10) ** len(str(a))
        a = a // 10
    result = "Armstrong"
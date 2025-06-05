s=input("Enter the string: ").strip()
l=[]
for i in s:
    if i not in l:
        l.append(i)
        print(f"{i} : {s.count(i)}")
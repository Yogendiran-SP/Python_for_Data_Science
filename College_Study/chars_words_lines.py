def counting(file):
    try:
        with open(file,"r") as f:
            content = f.read()
            chars = len(content)
            words = len(content.split())
            lines = content.count("\n") +1
            print("No. of Characters:",chars)
            print("No. of Words:",words)
            print("No. of Lines:",lines)
            f.close()
    except FileNotFoundError as e:
        print("Error:",e)

counting(input("Enter the filename: ").strip())
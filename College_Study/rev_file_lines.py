def reverse_printing(file):
    try:
        with open(file,"r") as f:
            content = f.readlines()
            for i in reversed(content):
                print(i.strip())
            f.close()
    except FileNotFoundError as fnfe:
        print("Error:",fnfe)

reverse_printing(input("Enter the filename: ").strip())

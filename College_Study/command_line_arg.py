import sys
if len(sys.argv)!=3:
    print("Usage: python command_line_arg.py <num1> <num2>")
    sys.exit()
num1 = float(sys.argv[1])
num2 = float(sys.argv[2])
res = num1+num2
print(f"The Sum of {num1} and {num2} is {res}")
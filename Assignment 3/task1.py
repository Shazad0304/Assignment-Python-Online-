fn = int(input("Please enter first number"));
sn = int(input("Please enter second number"));
op = input("Please enter operator");

if op == "+":
    print(fn+sn)
elif op == "-":
    print(fn-sn)
elif op == "/":
    print(fn/sn)
elif op == "%":
    print(fn%sn)
elif op == "**":
    print(fn**sn)
else:
    print("Incorrect Operator");

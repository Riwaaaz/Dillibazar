def sub(n1, n2):
    return n1 - n2

print("Please select operation -\n"
      "2. Subtract\n")

sel = int(input("Select operation (2): "))

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

if sel == 2:
    print(n1, "-", n2, "=", sub(n1, n2))
else:
    print("Invalid input")

def div(n1, n2):
    return n1 / n2

print("Please select operation -\n"
      "4. Divide\n")

sel = int(input("Select operation (4) "))

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))



if sel == 4:
    print(n1, "/", n2, "=", div(n1, n2))
else:
    print("Invalid input")
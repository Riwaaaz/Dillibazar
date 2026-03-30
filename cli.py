
def mul(n1, n2):
    return n1 * n2

print("Please select operation -\n"
      
      "1. Multiply\n")

sel = int(input("Select operation (1-4): "))

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

if sel == 1:
  
    print(n1, "*", n2, "=", mul(n1, n2))

else:
    print("Invalid input")
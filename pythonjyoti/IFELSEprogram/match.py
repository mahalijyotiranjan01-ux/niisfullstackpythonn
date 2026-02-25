num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose Operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")

choice = int(input("Enter your choice (1/2/3): "))
match choice:
    case 1:print("Result =", num1 + num2)
case 2:print("")


elif choice == 2:
    print("Result =", num1 - num2)
elif choice == 3:
    print("Result =", num1 * num2)
else:
    print("Invalid Choice")
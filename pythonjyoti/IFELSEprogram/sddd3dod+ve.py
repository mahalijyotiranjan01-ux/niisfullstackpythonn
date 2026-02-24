# Program to check digit type and sign of a number

num = int(input("Enter a number: "))
if num > 0:
    sign = "Positive (+ve)"
abs_num = abs(num)
if abs_num < 10:
    digit_type = "Single Digit"
elif abs_num < 100:
    digit_type = "Double Digit"
elif abs_num < 1000:
    digit_type = "Triple Digit"
else:
    digit_type = "More than Three Digits"

print("Number Type:", digit_type)
print("Sign:", sign)
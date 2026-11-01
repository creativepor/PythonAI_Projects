# Enter 3 numbers and check which is the largest

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the 2nd number: "))
num3 = int(input("Enter the 3rd number: "))

if(num1 > num2 and num1 > num3):
    print(f"The number {num1} is the largest")
elif(num2 > num1 and num2 > num3):
    print(f"The number {num2} is the largest")
else:
    print(f"The number {num3} is the largest")
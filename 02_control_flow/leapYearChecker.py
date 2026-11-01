# Check if a given number is leap year or not

year = int(input("Enter the Year you want to check: "))

if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The Year is a leap year")
else: 
    print("this is not a Leap year")    





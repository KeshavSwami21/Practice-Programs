year = int(input("Enter the year to check it is a leap year or not: "))

if (year % 400 == 0):
    print(f"{year} is a leap year.")
elif(year % 4 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
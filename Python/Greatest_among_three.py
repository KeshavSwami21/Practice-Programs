num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the Second number: "))
num3 = int(input("Enter the third number: "))
if (num1>num2):
    if(num1>num3):
        print(f"{num1} is greater then {num2}, {num3}.")
    else:
        print(f"{num3} is greater then {num1}, {num2}.")

elif(num2>num1):
    if (num2 > num3):
        print(f"{num2} is greater then {num1}, {num3}.")
    else:
        print(f"{num3} is greater then {num1}, {num2}.")

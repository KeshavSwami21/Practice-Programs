numbers = input("Enter the numbers to form a list and tuple from \nthem(Numbers should be"
                "separated from \'comma\'): ")
list = numbers.split(',')
tuple = tuple(list)

print(list)
print(tuple)
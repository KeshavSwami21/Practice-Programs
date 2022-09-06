# from ssl import RAND_egd


# for i in range(0, 6):
#     for j in range(6-i):
#         print(" ", end="")
#     for k in range(i):
#         print("*", end="  2q32353           ")
#     print()


# print("Flipped Triangle")

# num = 9
# for i in range(num, 0, -1):

#     for j in range(0, num-i):
#         print(end=" ")

#     for j in range(0, i):
#         print("*", end=" ")

#     print()
    
    

for row in range(7):
    for col in range(7):
        if(col == 6) or ((row!=0) & (col==5)) or ((row!=0 and row!=1) & (col==4)) or ((row!=0 and row!=1 and row!=2) & (col==4)):
            print("*", end=" ")
        else:
            print("  ", end="")
    print()
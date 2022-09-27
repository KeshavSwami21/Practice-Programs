class WGT:

    global weights
    weights = []

    def User_Input(self):
        N = int(input("Enter the number of balls thrown by geekina: "))

        for i in range(N):
            w = int(input(f"Enter the weight of {i+1} ball: "))
            weights.append(w)

        # print(weights)

    def Logic(self):
        # Calculating the weight of final big ball
        B_weight = sum(weights)
        print(
            f"The weight of the mega-snowball geek will throw at geekina in the end is: {B_weight}")


wgt = WGT()

wgt.User_Input()
wgt.Logic()

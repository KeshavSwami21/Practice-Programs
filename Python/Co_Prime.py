from math import gcd


class C_P:


    def Input(self):
        N = int(input("Enter the first number: "))
        M = int(input("Enter the second number: "))
    
        C_P.coprime(N, M)
    
    def coprime(N, M):
         
        if ( gcd(N, M) == 1):
            print("Co-Prime")
        else:
            print("Not Co-Prime")
        

cp = C_P()


cp.Input()
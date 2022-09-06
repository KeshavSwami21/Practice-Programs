n = int(input("Enter a number: "))

a = int("%d" %n)
b = int("%d%d" % (n,n))
c = int("%d%d%d" % (n,n,n))

print(a+b+c)

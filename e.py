import math
n = int(input("Enter value of n (between 0 to 51)"))
if(n<=51):
    txt = print("The value of pi to",n, "places is {:.{prec}f}".format(math.e,prec=n))
else:
    print("Enter a number between given values")
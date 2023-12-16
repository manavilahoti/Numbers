from math import pi

n = int(input("Enter value of n (between 0 to 49)"))
txt = print("The value of pi to",n, "places is {:.{prec}f}".format(pi,prec=n))
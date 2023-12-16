n_1 = 0 
n_2 = 1
n = int(input("Enter the value of n "))
def fibonacci(n):
    if n<=0:
        return("Invalid number")
    elif n==1:
        return(n_1)
    elif n==2:
        return(n_2)
    else:
        return int(fibonacci(n-1))+ int(fibonacci(n-2))
    
for i in range(1,n+1):
    result = fibonacci(i)
    print("The fibonacci series for", i, "terms is", result)
    

    
    




operation = input("State the operation to be performed (add, sub, multiply, divide, power, root) ")
x = int(input("Enter the value of x "))
y = int(input("Enter the value of y "))
def calculate(x,y):
    if(operation == "add"):
        return(x+y)
    elif(operation == "sub"):
        return(x-y)
    elif(operation == "multiply"):
        return(x*y)
    elif(operation == "divide"):
        return(x/y)
    elif(operation == "power"):
        return(x ** y)
    elif(operation == "root"):
        return(round(x ** (1/y)))
    else:
        return("Invalid number")
    
result = calculate(x,y)
print(f"The result of {operation} is {result}")
    


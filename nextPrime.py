n = 0
def is_Prime(number):
    if(number<=1):
        return("Not Prime")
    elif(number==2):
        return("Prime")
    else:
        for i in range(2, number-1):
            if(number%i == 0):
                return("Not Prime")
        return("Prime")

while True:
    x = input("Do you wish to continue the program (Enter 'y' or 'n') ")
    if x.lower()=="n":
        print("Exiting program")
        break
    n +=1
    result = is_Prime(n)
    print(f"{n} is {result}")

        

        
        
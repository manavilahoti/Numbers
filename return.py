cost = float(input("Enter the cost of product"))
amount = float(input("Enter the amount given"))
change = amount-cost

quarter_value = 0.25
dime_value = 0.10
nickel_value = 0.05
penny_value = 0.01

def return_amount(change):
    if(change<0):
        return("Insufficient balance provided")
    elif(change==0):
        return("No change required")
    else:
        quarter = int(change//quarter_value)
        change = change%quarter_value

        dime = int(change//dime_value)
        change = change%dime_value

        nickle = int(change//nickel_value)
        change = change%nickel_value

        penny = int((change/penny_value))

        result = (f"The change amount is {amount-cost:.2f} and it requires {quarter} quarters, {dime} dimes, {nickle} nickles and {penny} pennies")
        return result
print("The change amount is", change)  
value = return_amount(change)
print(value)
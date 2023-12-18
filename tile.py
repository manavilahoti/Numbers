h = float(input("Enter the height of the floor "))
w = float(input("Enter the weight of the floor "))
cost_of_tile = float(input("Enter the cost of a tile "))
number_of_tiles = h*w
def totalcost(cost_of_tile):
    total_cost = cost_of_tile * number_of_tiles
    return total_cost

result = totalcost(cost_of_tile)
print(f"The total cost of {number_of_tiles:.2f} is {result:.2f}")
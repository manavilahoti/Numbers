decimal = int(input("Enter a decimal value "))
def decimal_converter(decimal):
    binary_result = ""
    while(decimal>0):
        bits = decimal%2
        binary_result = str(bits) + binary_result
        decimal = decimal//2
    return binary_result
    
result_b = decimal_converter(decimal)
print(f"The binary equivalent for {decimal} is {result_b}")

binary = input("Enter a binary number ")
def binary_converter(binary):
    decimal_result = 0
    binary_num = binary[::-1]
    for i in range(len(binary_num)):
        if(binary_num[i] == "1"):
            decimal_result += 2**i
    return decimal_result

result_d = binary_converter(binary)
print(f"The decimal equivalent of {binary} is {result_d}")
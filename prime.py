n = int(input("Enter a number: "))
def prime_numbers(n):
    factor = []
    while n%2 == 0:
        factor.append(2)
        n = n//2

    for i in range(3, n+1,2):
        while(n%i == 0):
            factor.append(i)
            n = n//i
    
    return factor

result = prime_numbers(n)
print(f"The prime factors of {n} are: {result}")
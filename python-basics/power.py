def power(x, n):
    if n == 0:              # base case
        return 1
    return x * power(x, n - 1)   # recursive case

x = int(input("Enter base: "))
n = int(input("Enter exponent: "))
print(f"{x} ^ {n} =", power(x, n))

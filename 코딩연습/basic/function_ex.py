# n! = n * (n-1) * (n-2) * ... * 1

def factorial(n):
    output = 1

    for i in range(1, n+1):
        output *= i

    return output

print(factorial(5))
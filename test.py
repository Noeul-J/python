number = 1234
div = 10
result = 0

while number != 0:
    result = result * div
    result = result + number % div
    number = number / div

print(result)
numbers = []

for i in range(100, 1000):
    digit = i % 10
    ten = (i % 100 - i % 10) // 10
    hundred = (i - i % 100) // 100
    number = digit + ten + hundred
    if number % 10 == 0:
        numbers.append(i)
        
print(numbers)
print('The amount is: ' + str(len(numbers)))
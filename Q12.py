# Calculate the sum of digits of a given number

def sumOfDigits(num):
    sum = 0
    while(num>0):
        rem = num % 10
        sum += rem
        num = num// 10
        # // division operator that rounds off the value
    print(sum)

sumOfDigits(123)
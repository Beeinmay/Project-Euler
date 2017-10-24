#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

maxNumber  = int(input('Enter a maximum number: '))
multipleOne = int(input('Enter a multiple: '))
multipleTwo = int(input('Enter another multiple: '))

sum = 0
for num in range(maxNumber):
    if ( num % multipleOne == 0 ) or ( num % multipleTwo == 0 ):
        sum += num
print(sum)
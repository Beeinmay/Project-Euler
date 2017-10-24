#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

#References:
#https://stackoverflow.com/questions/9053545/finding-the-sum-of-even-valued-terms-in-fibonacci-sequence

numA = 0
numB = 1

maxNum = 4000000
total = 0

while numA < maxNum:
    numA, numB = numB, numA + numB
    if numA % 2 == 0:
        total += numA
    
print(total)

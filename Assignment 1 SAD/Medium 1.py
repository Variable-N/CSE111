#Medium 1

n=int(input('Enter the value of n: '))
firstValue = 0
secondValue = 1
while firstValue <= n :
    print (firstValue, end=" ")
    temp = firstValue
    firstValue = secondValue
    secondValue = secondValue + temp
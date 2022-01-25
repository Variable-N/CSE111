#Medium 3

num = int(input('Enter a number : '))
sum = 0
for index in range (int(num/2)+1) :
    if index != 0 :
        if  num % index == 0 :
            sum+= index
if sum == num :
    print ('Perfect')
else :
    print ('Not Perfect')
#Hard 3

import math
decimal_num = int(input("Enter a number: "))

#Converting decimal to binary but reversed 

reversed_binary_num = ""
while decimal_num > 1 :
    reversed_binary_num += str(decimal_num%2)
    decimal_num = math.floor(decimal_num/2)
reversed_binary_num += str(decimal_num)

#Counting the number of 1 in inversed binary number

length = len(reversed_binary_num)
count = 0
for i in range (length) :
    if reversed_binary_num[i] == '1' :
        count += 1

#Converting the smallest binary to decimal value

smallest_binary_number = ""
decimal = 0
if count == 0 :
    print (0)
else:
    while count!=0:
        smallest_binary_number += "1"
        count -= 1
    smallest_binary_number = int(smallest_binary_number)
    base = 1
    while smallest_binary_number != 0 :
        decimal+= base
        base = base * 2
        smallest_binary_number = int(smallest_binary_number/10)
    print(decimal)
    

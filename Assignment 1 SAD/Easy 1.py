#Easy 1
num = 3
count = 0
print ("The numbers that are  either divisible by 3 or 5 are : ")
while num <= 30 :
    if num % 3 == 0 or num % 5 == 0 :
        count+=1
        print (num, end = " ")
    num += 1
print("\nThe amount of these numbers is",count)
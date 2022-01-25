#Hard 1
digits = [0,0,0,0,0,0,0,0,0,0,0]
num = int(input("Enter a number: "))
count = 0
while num != 0 :
    if digits[num%10] == 0: 
        digits[num%10] = 1
        count+=1
    num = int(num/10)
print("The number of unique digit is:",count)
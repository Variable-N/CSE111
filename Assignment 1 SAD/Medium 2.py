#Medium 2

num = int(input('Please enter a number : '))
if num==0:
    print(0)
while num != 0 :
    print(num%10, end="")
    num = int(num/10)

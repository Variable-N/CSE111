#Easy 4

num = int(input("Enter a number: "))
divisor = 3
if num==1 or num%2==0:
    if num==2:
        print("Prime")
    else :
        print ('Non Prime')
else :
    prime =  True
    while divisor <= int(num/2)+1:
        if num%divisor == 0 :
            prime = False
        divisor+=2
    if prime :
        print ('Prime')
    else:
        print ('Non Prime')
        
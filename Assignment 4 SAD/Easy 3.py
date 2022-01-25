list = []
list.append(input('Please enter a number: '))
i=1
while i < 10 :
    number = input('Please enter another number: ')
    if number in list:
        print("Duplicate")
    else :
        list.append(number)
        i += 1


print("You have entered: ",end="")
for i in range(10):
    print(list[i], end = " ")
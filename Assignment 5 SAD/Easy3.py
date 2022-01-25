dictionary = {}
dictionary[0] = int(input('Please enter a number: '))
i=1
while i < 10 :
    number = int(input('Please enter another number: '))
    duplicate = False
    for j in dictionary :
        if dictionary[j] == number:
            print("Duplicate")
            duplicate = True
            break
    if not duplicate:
        dictionary[i] = number
        i += 1


print("You have entered: ",end="")
for i in range(10):
    print(dictionary[i], end = " ")
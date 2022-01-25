#Slide 1

word = input('Please enter something: ')
length = len(word)
for index in range (length-1,-1,-1):
    print(word[index],end="")
print()
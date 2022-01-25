#Slide 2

word = input('Please enter something: ')
index = len(word)-1
while index > -1 :
    print(word[index], end = "")
    index -= 1
print()
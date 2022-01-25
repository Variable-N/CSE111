string1 = input ()
string2 = input ()
list1 = string1.split(', ')
list2 = string2.split(', ')
list1.pop()
answer = list1+list2
print(answer)
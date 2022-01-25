list = []
number = input ()
while number != "STOP" :
    list.append(number)
    number = input()
unique = [list[0]]
for i in range(1,len(list),1) :
    if list[i] not in unique :
        unique.append(list[i])

for i in unique:
    print(i,'-',list.count(i),'times')


string1 = input()
d1 = {}
while string1 != "STOP" :
    number = int(string1)
    if number in d1 :
        d1[number] += 1
    else :
        d1[number] = 1
    string1 = input()
for i in d1:
    print(i,'-',d1[i],'times')

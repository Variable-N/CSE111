string1 = input()
string2= input()
common = ""
for i in string1:
    for j in string2:
        if i==j :
            common += i
if common == "" :
    print('Nothing in common')
else :
    print(common,end="")
    for j in string2:
        if j in common:
            print(j,end="")
    print()
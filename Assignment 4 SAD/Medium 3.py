string = input()
list1 = string.split(' ')
string = input()
list2 = string.split(' ')
ans = []
for i in list1 :
    for j in list2 :
        ans.append(int(i)*int(j))
print(ans)
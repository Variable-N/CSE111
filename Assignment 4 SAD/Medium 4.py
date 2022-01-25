n = int(input())
string = input()
list = string.split(',')
ans = []
for i in range (0,n,1):
    temp = []
    for j in range (0,len(list),1) :
        if j%n == i :
            temp.append(list[j])
    ans.append(temp)
print (ans)
string = input()
nk = string.split()
k = int(nk[1])
list1 = []
string = input()
list1 = string.split()
ans = 0
count = 0
for i in range (0,len(list1),1) :
    list1[i] = int(list1[i]) + k
    if list1[i] <= 5 :
        count+=1
    if count == 3:
        count = 0
        ans += 1
print(ans)

    
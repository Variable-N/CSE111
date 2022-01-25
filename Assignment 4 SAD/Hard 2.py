string = input()
small = []
capital = []
odd = []
even = []
for i in string :
    if ord(i) >= 97 and ord (i) <=122 :
        small.append(i)
    elif ord(i) >= 65 and ord (i) <=90 :
        capital.append(i)
    elif int(i)%2==0 :
        even.append(int(i))
    else :
        odd.append(int(i))
small.sort()
capital.sort()
even.sort()
odd.sort()
ans = ""
for i in small:
    ans+=i
for i in capital:
    ans+=i
for i in odd:
    ans+=str(i)
for i in even:
    ans+=str(i)
print(ans)

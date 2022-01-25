list1 = [i for i in input().split(', ')]
d1 = {}
for i in list1 :
    x = i.split(': ')
    d1[x[0]] = int(x[1])
list1 = [i for i in input().split(', ')]
d2 = {}
for i in list1 :
    x = i.split(': ')
    d2[x[0]] = int(x[1])
for i in d1 :
    if i in d2:
        d1[i] += d2 [i]
for i in d2 :
    if i not in d1:
        d1[i] = d2 [i]
print(d1)
tup = ()
for i in d1 :
    if d1[i] not in tup:
        temp = (d1[i],)
        tup += temp
tup = sorted(tup)
print("Values:", tup)

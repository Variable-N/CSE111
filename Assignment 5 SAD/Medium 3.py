list1 = [i for i in input().split(', ')]
d1 = {}
keys = []
values = []
for i in list1 :
    x = i.split(' : ')
    keys.append(x[0])
    if x[1] not in values:
        values.append(x[1])
    d1[x[0]] = x[1]
d2 = {}
for i in values:
        l1 = []
        for j in range (len(keys)) :
            if d1[keys[j]] == i:
                l1.append(keys[j])
        d2[i] = l1
print(d2)    
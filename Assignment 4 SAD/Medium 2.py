n = int(input ())
max = 0
for i in range (n):
    sum = 0
    string = input()
    list1 = string.split()
    for i in list1 :
        sum += int(i)
    if i == 0 or sum > max:
        max = sum
        a = list1
print(max)
print(a)
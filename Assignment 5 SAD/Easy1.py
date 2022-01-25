list = [i for i in input().split(', ')]
dictionary = {}
for i in list:
    x = i.split(': ')
    dictionary[x[0]] = int(x[1])

find = input()
while find != 'STOP' :
    ans = False
    find = int(find)
    for i in dictionary:
        if dictionary[i] == find :
            ans = True
            break
    print(ans)
    find = input()

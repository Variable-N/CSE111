list = [i for i in input().split(', ')]
dictionary = {}
maximum = ''
minimum = ''
first = True
for i in list :
    x = i.split(': ')
    if first:
        maximum = x[0]
        minimum = x[0]
        first = False
    dictionary[x[0]] = int(x[1])
    if dictionary[x[0]] > dictionary[maximum] :
        maximum = x[0]
    if dictionary[x[0]] < dictionary[minimum] :
        minimum = x[0]
print("Minimum:",minimum,"\nMaximum:",maximum)


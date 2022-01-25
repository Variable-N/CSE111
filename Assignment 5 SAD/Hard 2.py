def ekta_dictionary_banay_eita():
    d1 = {}
    d1['.'] = 1
    d1[','] = 11
    d1['?'] = 111
    d1['!'] = 1111
    d1[':'] = 11111
    d1[' '] = 0
    reset = 1
    key = 2
    for i in range(65,91,1):
        s = ""
        for j in range(reset):
            s+= str(key)
        reset += 1
        if reset == 4 :
            reset = 1
            key += 1
        d1[chr(i)] = int(s)
        if i == 83:
            d1['S'] = 7777
            reset = 1
    d1['Z'] = 9999
    return d1

d1 = ekta_dictionary_banay_eita()
string = input()
string = string.upper()
answer = ""
for i in string:
    answer += str(d1[i])
print(answer)

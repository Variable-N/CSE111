string = input ()
capital = 0
small = 0
for i in string :
    if ord(i) >= 65 and ord (i) <=90 :
        capital += 1
    elif ord (i) >= 97 and ord (i) <=122 :
        small += 1

if capital > small :
    print(string.upper())
else :
    print(string.lower())
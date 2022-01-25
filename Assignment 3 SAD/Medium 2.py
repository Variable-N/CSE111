string = input ()
number = False
word = False
mixed = False
for i in string:
    if ord(i) <=57 and ord(i) >=48 :
        number = True
    else :
        word = True
    if number == word :
        mixed = True
        break
if mixed :
    print ('MIXED')
elif word :
    print ('WORD')
else :
    print('NUMBER')
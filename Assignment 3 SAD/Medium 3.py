string = input ()
record = False
output = ""
for i in string :
    if ord(i) >= 65 and ord (i) <=90:
        if not record:
            record = True
        else :
            record = False
            break
    if record and ord(i) >= 97:
        output += i
if output == "" :
    print('BLANK')
else :
    print (output)
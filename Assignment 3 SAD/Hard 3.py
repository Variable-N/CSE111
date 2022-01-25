password = input()
lowercase = False
uppercase = False
digit = False
special = False
for i in password :
    if ord(i) >= 97 and ord (i) <=122 and not lowercase:
        lowercase = True
    elif  ord(i) >= 65 and ord (i) <=90 and not uppercase:
        uppercase = True
    elif ord(i) <=57 and ord(i) >=48 and not digit:
        digit = True
    elif ord(i) == 95 or ord(i) == 36 or ord(i) == 35 or ord(i) == 64 and not special:
        special = True

if lowercase and uppercase and digit and special :
    print ("OK")
if not lowercase :
    print ("Lowercase character missing")
if not uppercase :
    print ("Uppercase character missing")
if not digit :
    print ("Digit missing")
if not special :
    print ("Special character missing")
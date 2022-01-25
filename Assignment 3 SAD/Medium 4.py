string = input ()
too = string.find('too')
good = string.find('good')
if good - too == 4:
    newstring = string.replace('too good','excellent')
    print(newstring)
else :
    print(string)
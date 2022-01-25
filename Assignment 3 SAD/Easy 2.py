string = input()
reverse = ""
for i in range (len(string)-1,-1,-1) :
    reverse += string[i]
if reverse == string :
    print("True")
else :
    print("False")
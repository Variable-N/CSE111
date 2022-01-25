string = input()
count = 0
output = ""
for i in string :
    if i.lower() == 'a' or i.lower() == 'e' or i.lower() == 'i' or i.lower() == 'o' or i.lower() == 'u' :
        count +=1
    else :
        output += i
print(output , count , sep="")
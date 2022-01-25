string = input()
start =""
Segment=""
flag = False
for i in range (0,int(len(string)/2+1),1) :
    start += string[i]
    if string.endswith(start) :
        middleString = string[len(start):len(string)-len(start)]
        if start in middleString:
            Segment = start
            flag = True
if flag :    
    print(Segment)
else :
    print("Not Palindrome Substring")

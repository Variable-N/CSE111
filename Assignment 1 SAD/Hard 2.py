#Hard 2

line = int(input("Please enter a number: "))
for lineCount in range (1,line,1) :
    for space in range (0,line-lineCount,1) :
        print(" ",end = "")
    if lineCount == 1 :
        print("*",end = "")
    else :
        print("*",end = "")
        for space in range (1,2*(lineCount-1),1):
            print(" ", end = "")
        print("*",end = "")
    print("")

for star in range (1,2*line,1) :
    print("*",end = "")
print()
for lineCount in range (line-1,0,-1) :
    for space in range (0,line-lineCount,1) :
        print(" ",end = "")
    if lineCount == 1 :
        print("*",end = "")
    else :
        print("*",end = "")
        for space in range (1,2*(lineCount-1),1):
            print(" ", end = "")
        print("*",end = "")
    print("")
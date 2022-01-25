string = input()
while string != "STOP":
    list1 = string.split()
    difference = len(list1)-1
    ub = True
    x = []
    for i in range (0,len(list1)-1,1) :
        x.append(abs(int(list1[i])-int(list1[i+1])))
    x.sort()
    for i in range (len(x)-1) :
        if x[i+1] - x[i] != 1 :
            ub = False
            break
    if ub :
        print('UB Jumper')
    else :
        print("Not UB Jumper")
    string = input()
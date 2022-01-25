def fracture_of_division(x,y) :
    if y==0 :
        return 0
    elif x/y == 0 :
        return 0
    else :
        return x/y-int(x/y)
        
a = float(input())
b = float(input())
print (fracture_of_division(a,b)) 
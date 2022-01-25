def homemade_for_loop (st, en, inc)  :
    sum=0
    while st<en :
        sum+= st
        st+=inc
    return sum

startValue = int(input())
endValue = int(input())
increment = int(input())
print(homemade_for_loop(startValue,endValue,increment))
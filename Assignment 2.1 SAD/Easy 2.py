def BMI (weight, height) :
    bmi = weight/(height/100*height/100)
    print ("Score is","%.1f"%bmi,end=". ")
    if bmi < 18.5 :
        print('You are Underweight')
    elif bmi < 25 :
        print('You are Normal')
    elif bmi <= 30 :
        print('You are Overweight')
    else :
        print('You are Obese')




h = float(input())
w = float(input())
BMI(w,h)
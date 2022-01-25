import datetime 
from datetime import date
#def date_conversion (temp) : 
#   return date(int(temp[0:4]),int(temp[5:7]),int(temp[8:10]))

def bonus (name,salary,givenDate) :
    today_date = date.today()
    join_date = date(int(givenDate[0:4]),int(givenDate[5:7]),int(givenDate[8:10]))
    serviced = (today_date - join_date).days
    if serviced < 365*5 :
        bonusSalary = salary *0.1
    elif serviced > 10*365 :
        bonusSalary = salary * 0.15 + 15000
    else :
        bonusSalary = salary * 0.1 + 5000
    name+=':'
    print (name, int(bonusSalary))
 
employee = "this was way too hard for begginers"
while True :
    employee = input()
    if employee == "" :
        break
    salary = int (input())
    joinDate = input()
    bonus(employee,salary,joinDate)

    #TIMESTAMP('Alice', 20000, '2017-03-21', 'Bob', 50000, '2007-05-10')
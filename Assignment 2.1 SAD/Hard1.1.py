import datetime 
from datetime import date
def date_conversion (temp) : 
    return date(int(temp[0:4]),int(temp[5:7]),int(temp[8:10]))

def bonus (*data) :
    total_data = len(data)
    today_date = date.today()
    for i in range (0,total_data,3) :
        name = data[i]
        salary = data[i+1]
        serviced = (today_date-date_conversion(data[i+2])).days
        if serviced < 365*5 :
            bonusSalary = salary *0.1
        elif serviced > 10*365 :
            bonusSalary = salary * 0.15 + 15000
        else :
            bonusSalary = salary * 0.1 + 5000
        name+=':'
        print (name, int(bonusSalary))

bonus('Alice', 20000, '2017-03-21', 'Bob', 50000, '2015-12-23')
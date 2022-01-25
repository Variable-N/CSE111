class Dates:
    def __init__(self,date):
        self.date = date
    @classmethod
    def toDashDate(cls,slashDate): #   05/09/2020
        dashDate = ""              #   05-09-2020
        for i in slashDate:
            if i != '/':
                dashDate += i
            else :
                dashDate += '-'
        return Dates(dashDate)
    def getDate(self):
        return self.date

date1 = Dates("05-09-2020")
dateFromDB = "05/09/2020"
date2= Dates.toDashDate(dateFromDB)
if (date1.getDate() == date2.getDate() ):
    print("Equal")
else:
    print("Unequal")

print("""\n\nExplanation : date2 object parameter has been changed from slash to dash. 
So both date1.name and date2.name object has the same string value. This is why, 
when we compare the getDate method of both objects, we get 'Equal' as output.""")
#Subtask 1
class Student:
    ID = 0
    #Subtask 2
    def __init__(self,name,department,age,cgpa):
        self.name = name
        self.department = department
        self.age = age
        self.cgpa = cgpa
        Student.ID += 1
    #Subtask 3
    def get_details (self) :
        print('ID:',Student.ID,'\nName:',self.name,'\nDepartment:',self.department,'\nAge:',self.age,'\nCGPA:',self.cgpa)
    #Subtask 4
    @classmethod
    def from_String(cls,string):
        info = string.split('-')
        return Student(info[0],info[1],info[2],info[3])

s1 = Student("Samin", "CSE", 21, 3.91)
s1.get_details()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.get_details()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.get_details()
print("-----------------------")
s4 = Student.from_String("Sumaiya-BBA-23-3.96")
s4.get_details()


#Subtask 5
print("\nSubtask 5:\n")
print('A class variable is declared when the class is being created whereas an instance variable is declared when an object is being created.')
print('Class variables have same value for all objects but instance variables have different values for different objects.')

#Subtask 6
print("\nSubtask 6:\n")
print('Instance Method: Instance method must be called by an object. It takes self as a parameter')
print('Class Method: Class method must be called by a class or object. It takes cls as a parameter')
print('Static Method: Static method can be called without an object or class. It may not take self or cls as a parameter.')
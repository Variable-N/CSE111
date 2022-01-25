#Hard Task_01
#Author Aditi Saha Ria
#ID : 20101238
def bonus_salary(*args):
    count = 0
    for i in args:
        count += 1
   
    i = 0
    while i < len(args)-2:
        salary = int(args[i+1])
        joining_day = ''
        bonus = 0
        list=args[i+2].split('-')
        joining_day = list[0]
        joining_day = 2020 - int(joining_day)
        if joining_day < 5:
            bonus = salary * 0.1
        elif joining_day < 11:
            bonus = (salary * 0.1) + 5000
        else:
            bonus = (salary * 0.15) + 15000
        if i+3 == count:
            print(f'{args[i]}: {bonus}')
        else:
            print(f'{args[i]}: {bonus}', end=', ')
        i += 3

bonus_salary('Alice', 20000, '2017-03-21', 'Bob', 50000, '2007-05-10')
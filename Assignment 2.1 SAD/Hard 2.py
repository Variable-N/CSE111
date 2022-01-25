def time (days):
    remaining_days = days%365
    print (int(days/365), 'years, ', int(remaining_days/30), 'months and ', remaining_days%30, 'days' )

day = int(input())
time(day)
#convert given number of days into weeks and days.

days = int(input("enter the numbers of days to be convert into weeks and days"))
weeks = days//7
daysleft = days%7
print("the number of weeks are :",weeks,"\n the days left are  :",daysleft)

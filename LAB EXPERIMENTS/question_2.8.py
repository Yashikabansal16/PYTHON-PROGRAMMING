# take input from user
day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

# check whether the year is leap year or not
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
   leap = True
else: 
   leap = False

# checking number of days in a month
if month == 2:
   if leap:
      days = 29
   else:
      days = 28
elif month == 4 or month == 6 or month == 9 or month == 11:
   days = 30
else:
   days = 31

# calculate next day
if day<days:
   day += 1
else:
   day = 1
   month += 1
   if month > 12:
       month = 1
       year += 1

# show result
print("Next day:",day,"\nNext month:",month,"\nNext year: ",year)


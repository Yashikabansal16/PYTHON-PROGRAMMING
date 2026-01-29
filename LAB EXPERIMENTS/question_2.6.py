# taking input from user
year = int(input("Enter a year: "))

# check condition for leap year
if(year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
   print(year,"is a leap year")
else:
   print(year,"is not a leap year")


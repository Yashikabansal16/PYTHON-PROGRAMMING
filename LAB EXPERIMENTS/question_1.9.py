# input variable time
time = int(input("Enter the time in seconds: "))

# perform conversions
hour = time // 3600
minute = (time % 3600) // 60
seconds = time % 60

# print the result
print("Hour:",hour,"\nMinute:",minute,"\nSeconds:",seconds)
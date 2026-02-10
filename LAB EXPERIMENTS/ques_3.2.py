# taking input from user
num = int(input("Enter a number: "))
temp = num
sum = 0
digits = len(str(num))

while temp>0:
    digit = temp % 10
    sum = sum + digit**digits
    temp = temp // 10

# display result
if sum == num:
   print(num,"is a Armstrong number.")
else:
   print(num," is not a Armstrong number.")
    

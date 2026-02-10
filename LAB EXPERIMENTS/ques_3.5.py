# taking input from the user
num = int(input("Enter a number: "))
temp = num
rev = 0

# checking whether a number is palindrome or not
while temp > 0:
      digit = temp % 10
      rev = rev * 10 + digit
      temp = temp // 10

# display result
if rev == num:
   print(num,"is a palindrome number.")
else:
   print(num,"is not a palindrome number.")


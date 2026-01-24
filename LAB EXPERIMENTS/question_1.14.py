# enter sequence and num to find
sequence = (10,56,78,89)
num = int(input("Enter a number to find in sequence:"))

# membership operator
if num in sequence:
   print(num,"is present in sequence")
else:
   print(num,"is not present in sequence")
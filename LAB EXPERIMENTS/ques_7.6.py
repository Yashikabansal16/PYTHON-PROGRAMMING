try:
    filename = input("Enter file name: ")
    
    try:
        with open(filename,"r") as file:
            count = int(file.read())
    except FileNotFoundError:
        print("File Found")
        count = 0
    except ValueError:
        print("Value Excepted")
        count = 0
    
    count += 1

except Exception as e:
    print("Error code: ",e)

file = open("test_data.txt","w")
file.write(str(count))
file.close()

print("Program Executed",count,"times") 
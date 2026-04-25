# Defining a Class
class Point:
    # use constructor to initialize x and y values
    def __init__(self,x,y):
        self.x = x  # assigning x values to object
        self.y = y  # assigning y values to object 
        
    def __add__(self,other):
        x = self.x + other.x # add x coordinates
        y = self.y + other.y # add y coordinates
        return Point(x,y) # return new point 
    
    def display(self):
        print(f"Point(x={self.x}, y={self.y})") # print values

# create first object        
P1 = Point(10,20)
# create second object 
P2 = Point(12,15)

# add two objects 
P3 = P1 + P2

# display the result
P3.display()

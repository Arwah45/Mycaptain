#task1
from math import pi
r = float(input("Enter radius of the circle: "))
print("The area of the circle is ",pi*r*r)
#task2
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))

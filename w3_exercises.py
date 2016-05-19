#http://www.w3resource.com/python-exercises/python-basic-exercises.php
#get python version
import sys
print (sys.version)

#display current date and time 

import datetime #time module is better to get time wrt epoch
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

#area of a circle with user input
'''
from math import pi
r = float(input ("Input the radius of the circle : ")) #interactive user input instead of sysarg
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))g
'''


# Creat a list and a tuble from a string
splitlist=[]
splittuple=()
string=input("Input a comma separated list of numbers :")
splitlist=string.split(",")
print (splitlist)
splittuple=tuple(splitlist) 

#syntax.py


#function definition
def Whtnum (List1):
#Learning if Else
    if List1[1] != 13:
        print ('Not 13')
    elif List1[2]==14:
        print('14')
    else :
        print('13')


#Variable assignment
loop=5

#Raw input example
#name= raw_input('What is your name\n')
#print ('Hello %s' %name)

#for loop range example
print ('For loop and xrange example ; Print \"Hello World\" %d times' % loop)
for i in range(loop):
    print ('Hello World')


print ('\n')
#List examples
List1= [12,13,14,15]

#Enumerate example
print('Enumerate example')
for i, num in enumerate (List1):
    print (num)
print ('\n')

#function call with argument
print('Function with if-else example')
Whtnum(List1)
print ('\n')

#tuples example
print ('tuples example')
a,b = (2,3)
print ('a,b = (2,3)')
print ('a=%d'%a)
print ('b=%d'%b)
print ('\n')


    
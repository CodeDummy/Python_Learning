#Helloworld.py

def Whtnum (List1):
#Learning if Else
    if List1[1] != 13:
        print ('Not 13')
    else :
        print('13')


#for loop range example
print('For loop and xrange example ; Print \"Hello World\" 5 times')
for i in xrange(5):
    print ('Hello World')

List1= [12,13,14,15]

print('Enumerate example')
for i, num in enumerate (List1):
    print (num)
print('Function with if-else example')
Whtnum(List1)


    
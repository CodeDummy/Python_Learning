# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'
def donuts(count):
  # +++your code here+++
  if (count<10):
     return ( 'Number of donuts: ' + str(count))
  else :
     return  ('Number of donuts: many')
  

#donuts(6)


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = (' OK ')
  else:
    prefix = ('  X ')
  print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))



#Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
  print ('donuts')
  # Each line calls donuts, compares its result to the expected for that call.
  test(donuts(4), 'Number of donuts: 4')
  test(donuts(9), 'Number of donuts: 9')
  test(donuts(10), 'Number of donuts: many')
  test(donuts(99), 'Number of donuts: many')





# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
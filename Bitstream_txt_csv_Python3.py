import sys,re

args = sys.argv
#Accept and validate the arguments - Berk				
if len(args) != 2:
	print ("\nPlease provide the arguments as follows: filename \n")
	sys.exit(1)

file_to_open = args[1]
try:
	signal = open(file_to_open, "r")
	lines = signal.readlines()
	signal.close()
except:
	print ("\nPlease check the provided filename, either it doesn't exist or it can't be read\n")	
	sys.exit(1)

#Name new file to file_to_open.csv 
if re.search('/', file_to_open):
	file_to_open = file_to_open.split('/')[-1]
if re.search('\.', file_to_open):
	filename = file_to_open.split('.')[0]
filename += ".csv"

#Read Binary file		
newline=''
signal = open(file_to_open, "r")
lines = signal.readlines()
signal.close()

#Open csv file and write comma separated data in to it
output = open(filename, "w")

for line in lines :
    line = re.sub("\t",",", line) #Replace \t with Commas
    newline+=line

output.write(newline)
output.close()

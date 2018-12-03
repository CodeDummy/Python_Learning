#%% [markdown]
# ##Script to verify starfish data contains all conditions covered for each parameter.
# There are 2 parts to this problem,
# 
#%% [markdown]
# 1.Verify that each spec_id in the xmap file has all conditions.Min-Max spec parameter should have all conditions
#   Typ specs need only typ conditions
# 
#   
#%% [markdown]
# 2.Check datalog ,so that each parameter has data for all conditions  
#%% [markdown]
# Conditions for MIN-MAX and Typ must be defined somewhere May be in the xmap file as a comment
# 
# 
#%% [markdown]
# Algo:
#     Read Xmap.csv , extract FC superset and generate all combinations and count 
#  
# Git test   




#%%
import pandas as pd 
import itertools

#function to check if a char is a number
def is_number(n): 
    is_number = True
    try:
        num = complex(n)                              #v type-casting the number here as `complex`, instead of `float`
        is_number = num == num
    except ValueError:
        is_number = False
    return is_number

#function to get all combinations of conditions in 1 row,takes a list of strings where each string is 
#1 column (eg: '[9,10,11,12,20,21]' will be 1 string in the list, followed by other columns)
#the function returns a list conditions

def get_listofconditions_tuples (list_of_stringList):
    list_conditions=[]
    for string in list_of_stringList:
        string = string[1:(len(string)-1)]            #remove square brackets on both ends
        list_of_char=string.split(',')                #split the strings at ','
        list_numbers=[]
        list_strings=[]
        for number in list_of_char:
            if(is_number(number)):
                list_numbers.append(float(number))    #if the substring is a number , add it to a list of numbers
            else:
                list_strings.append(number)           #else to a list of strings
        if(len(list_numbers)>0):                      #add only non-empty lists to the master list
            list_conditions.append(list_numbers)
        elif (len(list_strings)>0) :
            list_conditions.append(list_strings)
    return list_conditions          
   
   
def combinations (list_conditions):
    combinations_list=[]
    for tuple_list in itertools.product(*list_conditions):
        combinations_list.append(tuple_list)
        #print (combinations_list)
    return combinations_list

PATH_FOR_MAPPINGFILE='C://Users//a0406675//Documents//XmapVerify//Mapping.csv'
df = pd.read_csv(PATH_FOR_MAPPINGFILE)  #read the mapping file 

#TODO
# need to make this more generic by detecting the FC_columns ; dropping the xmap required columns instead of hard coding 
# FC columns like below
drop_columns=df[['SPEC_ID','fs(MHz)','Temp(degC)','VDD(V)','InputDrive','MCE(LogicLevel)']]
Conditions=drop_columns[0:8] # rows 0 to 7 of the mapfile 

#TODO
# make a list of lists for all 7 rows and iterate over it 
#x = [[] for i in range(3)]
list_of_stringList=[]
#FIXME the for loop is only handling 1 row , make it handle multiple rows
number_of_columns=len(Conditions.columns)
for x in range(1,number_of_columns):
    list_of_stringList.append(Conditions.iloc[1,x])

list_conditions = get_listofconditions_tuples(list_of_stringList) 
combinations_list= combinations(list_conditions) 
print(len(combinations_list))
print(combinations_list)
#
#
#
#%%
list_of_stringList


#%%

#double multiplication signs raise numerics to the power

from itertools import count
from random import choice


print(2**3)
#expected output:8
print((7+5)*3)
#CTRL + F5 to run file

base_pay = 15
tips = 40
format_float = "{:.2f}".format(tips)
hours_worked = 40

print("Checking to see if github desktop is working!")
print("double checking!")


#1.1 Declare a varaible with your first and last name, use indexing to get your initials
first_name = "sean"
last_name = "magennis"
print(first_name[0].capitalize(),last_name[0].capitalize())
#1.2 Declare a variable with a country name, use indexing to get the first 3 letters of the country
choice = "ireland"
print(choice[0:3])
#1.3 Declare a string variable to hold the name of a country. Use indexing to print the last three letters of the country
country = "germany"
print(country[-3:])

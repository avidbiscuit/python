# -*- coding: utf-8 -*-
"""
Lab 03 - Variables - Collections.

This is the sample file for Lab 03
"""
first_name = "John"
last_name = "Smith"
age = 21
address = "Dundalk"
hourly_rate = 15.55


customer = ["Jane","Smith",21]

# Part 3
counties = ("Antrim","Armagh","Carlow","Cavan","Clare","Cork","Donegal","Down","Dublin","Fermanagh","Galway","Kerry","Kildare","Kilkenny","Laois","Leitrim","Limerick","Derry","Longford","Louth","Mayo","Meath","Monaghan","Offaly","Roscommon","Sligo","Tipperary","Tyrone","Waterford","Westmeath","Wexford","Wicklow")
county_towns = ("Ballymena","Armagh","Carlow","Cavan","Ennis","Cork","Lifford","Downpatrick","Dublin","Enniskillen","Galway","Tralee","Naas","Kilkenny","Portlaoise","Carrick-on-Shannon","Limerick","Coleraine","Longford","Dundalk","Castlebar","Navan",
"Monaghan","Tullamore","Roscommon","Sligo","Nenagh","Omagh","Dungarvan","Mullingar","Wexford","Wicklow")
# Part 4
income_tax = {"individual": 35300, "one-parent-family": 39300, "married-couples": 44300 , "low_rate": 20, "high-rate": 40}


print("******************* Task 1 ******************* ")
print("The tyepe of first_name is %s and its length is %d" %(type(first_name),len(first_name)))
print("The tyepe of last_name is %s and its length is %d" %(type(last_name),len(last_name)))
print("The tyepe of age is %s and you cannot get the length of this type" %(type(age)))
print("The tyepe of address is %s and its length is %d" %(type(address),len(address)))
print("The tyepe of hourly_rate is %s and you cannot get the length of this type" %(type(hourly_rate)))
print("The tyepe of customer is %s and its length is %d" %(type(customer),len(customer)))
print("The tyepe of counties is %s and its length is %d" %(type(counties),len(counties)))
print("The tyepe of county_towns is %s and its length is %d" %(type(county_towns),len(county_towns)))
print("The tyepe of income_tax is %s and its length is %d" %(type(income_tax),len(income_tax)))



print("******************* Task 2.1 ******************* ")
message = "Hello " + customer[0] + " " + customer[1] + ", how are you?"
print(message)

print("******************* Task 2.2 ******************* ")
print("Customer before append ", customer)
customer.append("Dublin Road, Dundalk")
print("Customer after append ", customer)

print("******************* Task 2.3 ******************* ")
#customer.reverse()
#print(customer)
#customer.reverse()
#print(customer)

# alternative method to use indexing
print(customer[::-1])
print(customer)

print("******************* Task 2.4 ******************* ")
print(customer[0] +" : "+  customer[-1])

print("******************* Task 2.5 ******************* ")
del(customer[-1])
print(customer)

print("******************* Task 2.6 ******************* ")
print(customer[0] +" : "+  str(customer[-1]))


print("******************* Task 3.1 ******************* ")

'''
county_from = input("Please enter the county you are from: ")
county_from = county_from.title()

try:
    county_index = counties.index(county_from)
    print("Hello I am from county " + counties[county_index] +", how are you?")
except:
    print("Something went wrong: ")


print("******************* Task 3.2 ******************* ")
print("The county town for county " + counties[county_index] + " is " +  county_towns[county_index])

'''

print("******************* Task 3.3 ******************* ")

new_county_tuple = counties + county_towns
print(new_county_tuple)

print("******************* Task 3.4 ******************* ")
# Cannot append to a tuple, they are fixed and cannot change once created

print("******************* Task 3.5 ******************* ")
name_tuple = ("Shane",)
print(type(name_tuple))




print("******************* Task 4.1 ******************* ")
#In the sample file there is a pre-declared dictionary income_tax, write a script to: print the value for the
#“individual” tax band.

print("There are two ways to get the value from a dictionary, one is to use the key name associated with the value")
val = income_tax["individual"]
print("The individual tax rate is %d" %(val))

print("the second safer way is to use get method")
val = income_tax.get("individual", "Error")
print("The individual tax rate is %d" %(val))

print("If we use get with an invalid key, it returns the default value")
val = income_tax.get("WrongKey", "Error")
print("The individual tax rate is %s" %(val))


print("******************* Task 4.2 ******************* ")
# Write a script to append “rich_rate” with a value of 50 to it.

# simply assign the value to the key
income_tax["rich_rate"] = 50
print(income_tax)

print("******************* Task 4.3 ******************* ")
#Write a script to copy the dictionary into a new dictionary called scottish_tax
scottish_tax = income_tax.copy()
print(scottish_tax)


print("******************* Task 4.4 ******************* ")
# Write a script to remove rich_rate from scottish_tax, print both dictionaries. Is rich_rate
# removed from both?

# delete rich_rate
del(scottish_tax["rich_rate"])
print("scottish_tax is {0}".format(scottish_tax))
print()
print("income_tax is {0}".format(income_tax))
print()
print("rich_rate is only removed from scottish_tax")



print("******************* Task 4.5 ******************* ")
#Create your own dictionary for an employee, include name, salary, address, position etc.
#demonstrate this to your lecturer. 

employee = {"name": "Gemma", "salary": 135300, "address" : "Dublin Road, Dundalk", "position" : "Chief Executive" }
print("Hello my name is %s I am a %s and I earn €%d per annum" %(employee["name"], employee["position"],employee["salary"]))



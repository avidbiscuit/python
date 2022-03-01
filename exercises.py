#double multiplication signs raise numerics to the power
from email.mime import base
from functools import total_ordering


print(2**3)
#expected output:8
print((7+5)*3)
#CTRL + F5 to run file

base_pay = 15
tips = float(input("Please input tips earned: "))
format_float = "{:.2f}".format(tips)
hours_worked = int(input("Please input your hours worked: "))
print("€", (base_pay *hours_worked) + format_float)
print("Checking to see if github desktop is working!")

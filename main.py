from termcolor import colored
import sys
from strings import *
#giving details to user
print(colored("This is a python based calculator","yellow"))


def start_calculation():
    print(colored('"plese type integer only in the place of Numericals"',"red"))
    number_1 = int(input("Enter the first Number:"))
    number_2 = int(input("Enter the second Number:"))
    operation = input("Enter the operation:")
    if operation == '+':
        print(colored("[*]","green"),"Answer is:"+str(number_1+number_2))
    elif operation == '-':
        pass
    elif operation == 'x' or '×' or 'X':
        pass
    elif operatiob == '/':
        pass
    
#function for input checking;
def start_functioning(user_input):
    if user_input == '-h':
        print(help_txt)
    if user_input == 'work':
        start_calculation()
    
    
    
while True:
    Function = input(colored("What do you want to do:","green"))
    start_functioning(Function)


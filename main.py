from termcolor import colored
import sys
from strings import *
#giving details to user
print(colored("    ====================================\n     This is a python based calculator\n       type 'q' to quit from anyware!\
\n    ====================================","yellow"))


def start_calculation():
    print(colored('    "plese type integer only in the place of Numericals"',"red"))
    try:
        number_1 = int(input(colored("  [+]Enter the first Number:",'green')))
        number_2 = int(input(colored("  [+]Enter the second Number:",'green')))
    except ValueError:
        print(colored("     Exiting.....","yellow"))
        exit(1)
    operation = input(colored("  [+]Enter the operation:",'green'))

    
    if operation == '+':
       print(colored("["+str(number_1)+"+"+str(number_2)+"]","green"),"Answer is:",colored(str(number_1+number_2),'green'))
    elif operation == '-':
        print(colored("["+str(number_1)+"-"+str(number_2)+"]","green"),"Answer is:",colored(str(number_1-number_2),'green'))
    elif operation == "*" or operation == 'x':
        print(colored("["+str(number_1)+"x"+str(number_2)+"]","green"),"Answer is:",colored(str(number_1*number_2),'green'))
    elif operation == '÷' or operation == '/':
        print(colored("["+str(number_1)+"÷"+str(number_2)+"]","green"),"Answer is:",colored(str(number_1/number_2),'green'))
    elif operation == 'q':
        exit(1)

#function for input checking;
def start_functioning(user_input):
    if user_input == 'h':
        print(help_txt)
    
    elif user_input == 'c':
        start_calculation()
    
    elif user_input == 'q':
        print(colored("     Exiting.....","yellow"))
        exit(1)

while True:
     Function = input(colored("    Do you want to start a calculator or help text(c/h):","green"))
     start_functioning(Function)
    


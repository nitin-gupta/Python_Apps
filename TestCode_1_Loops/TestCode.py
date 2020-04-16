# This is the test code which performs the following
# a) Detects the Python interpreter version at runtime
# b) Depending upon the Python version, calls the main function

import sys

l_welcome = "Welcome to the World of Python-Loops (for, switch, ifelse)" 
i = 0

# Defining main function 
def main1(): 
    print(l_welcome) 
  
def major_loop():
    s = PythonSwitchStatement()
    print(s.switch(1))


def minor_loop():
    # For loop where l_ctr varies from 0 to 10 with increment of 1
    for l_ctr in range(0,10,1):
        print("Minorloop-1 : " + str(l_ctr))
    # For loop where l_ctr varies from 0 to 10 with increment of 2
    for l_ctr in range(0,10,2):
        print("Minorloop-2 : " + str(l_ctr))
    # For loop where l_ctr varies from 10 to 0 with decrement of 1
    for l_ctr in range(10,-1,-1):
        print("Minorloop-3 : " + str(l_ctr))
    # For loop where l_ctr varies from 20 to 10 with decrement of 2
    for l_ctr in range(20,8,-2):
        print("Minorloop-4 : " + str(l_ctr)) 

class PythonSwitchStatement:

    def switch(self, month):
        default = "Incorrect month"
        return getattr(self, 'case_' + str(month), lambda: default)()

    def case_1(self):
        print("January")
        return "January"

    def case_2(self):
        return "February"

    def case_3(self):
        return "March"

    def case_4(self):
        return "April"

    def case_5(self):
        return "May"

    def case_6(self):
        return "June"

print("Detecting Python version....")
print (sys.version)
print("Version info.")
print (sys.version_info)

if(sys.version_info[0] >= 3):
    print("Result : Python Version 3")
    main1()
else:    
    print("Python Version 2")
    # Using the special variable  
    # __name__ 
    if __name__=="__main__": 
        main1() 
while (i < 10):
    major_loop()
    minor_loop()   
    i+=1
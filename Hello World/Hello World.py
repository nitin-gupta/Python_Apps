# This is the test code which performs the following
# a) Detects the Python interpreter version at runtime
# b) Depending upon the Python version, calls the main function

import sys

l_welcome = "Welcome to the World of Python" 
  
# Defining main function 
def main1(): 
    print(l_welcome) 
  
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
   
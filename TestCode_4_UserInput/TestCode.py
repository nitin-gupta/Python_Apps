# This is the test code which performs the following
# a) Detects the Python interpreter version at runtime
# b) Depending upon the Python version, calls the main function
# c) Take the input by the user to calculate the square, cube and exponential

import sys
import threading
import time, datetime
from threading import Event, Thread
import GlobalFunc
import GlobalVars

l_welcome = "Welcome to the World of Python-Timer Interrupt" 
i = 0
WAIT_SECONDS = 0.01

class RepeatedTimer:

    """Repeat `function` every `interval` seconds."""

    def __init__(self, interval, function, *args, **kwargs):
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.start = time.time()
        self.event = Event()
        self.thread = Thread(target=self._target)
        self.thread.start()

    def _target(self):
        while not self.event.wait(self._time):
            self.function(*self.args, **self.kwargs)

    @property
    def _time(self):
        return self.interval - ((time.time() - self.start) % self.interval)

    def stop(self):
        self.event.set()
        self.thread.join()


    #
  


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

# Defining main function 
def main1(): 
    print(l_welcome) 
    print(time.ctime())
    #threading.Timer(WAIT_SECONDS, major_loop).start()

def foo():
    #print("Call foo")
    GlobalFunc.major_loop()
    threading.Timer(WAIT_SECONDS, foo).start()  

print("Detecting Python version....")
print (sys.version)
print("Version info.")
print (sys.version_info)


# Auto Detection of Python Interpreter
'''
if(sys.version_info[0] >= 3):
    print("Result : Python Version 3")
    main1()
    major_loop()
else:    
    print("Python Version 2")
    # Using the special variable  
    # __name__ 
    if __name__=="__main__": 
        main1() 
'''
if __name__ == "__main__":
    GlobalVars.g_state_flag = False
    GlobalVars.g_state_ctr = 0

    print(GlobalVars.g_state_flag)
    print(GlobalVars.g_state_ctr)
    l_value = input("Please enter the number : ")
    l_power_val = input("Please input the exponential value : ")

    print("Square Val : " + str(GlobalFunc.func_square(int(l_value))))
    print("Cube Val : " + str(GlobalFunc.func_cube(int(l_value))))
    print("Exponential Val : " + str(GlobalFunc.func_exponential(int(l_value),int(l_power_val))))
    
    foo()

    while True:
        time.sleep(10.00)
        print("In while : " + str(time.ctime()))


    


        
    
# This is the test code which performs the following
# a) Detects the Python interpreter version at runtime
# b) Depending upon the Python version, calls the main function

import sys
import threading
import time, datetime
from threading import Event, Thread

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
  
def major_loop():
    #g_flag = False
    #s = PythonSwitchStatement()
    #print(s.switch(1) + ":" + str(datetime.datetime.now()))
    #print('hello {} ({:.4f})'.format(s,time.time()))
    print("Func :" +  str(datetime.datetime.now()))

    #if(g_flag == False):
    #    print("Func :" +  str(datetime.datetime.now()))
    #    g_flag = True
    #else:
    #    g_flag = False
    #    print("Func :" +  str(datetime.datetime.now()))
    

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

# Defining main function 
def main1(): 
    print(l_welcome) 
    print(time.ctime())
    #threading.Timer(WAIT_SECONDS, major_loop).start()

def foo():
    #print("Call foo")
    major_loop()
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
    foo()

    while True:
        time.sleep(0.01)
        print("In while : " + str(time.ctime()))


    


        
    
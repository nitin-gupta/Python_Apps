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
import serial.tools.list_ports

global g_serialport

l_welcome = "Welcome to the World of Python-Serial Port connection" 
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

    #print(GlobalVars.g_state_flag)
    #print(GlobalVars.g_state_ctr)
    #print("Method-1")
    #print(list(serial.tools.list_ports.comports()))
    #print("Method-1")
    #print([comport.device for comport in serial.tools.list_ports.comports()])
    #print("Method-3")
    #print(port for port in serial.tools.list_ports.comports())
    print("Method-2")
    ports = serial.tools.list_ports.comports()
    g_serialport = serial.Serial()
    g_serialport.baudrate = 19200

    for port, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(port, desc, hwid))
        try:          
            g_serialport.port = port
            g_serialport.timeout = 10
            print("Trying to Open : " + port)
            g_serialport.open()
            if (g_serialport.is_open == True):  
                print(port + " opened")
                g_serialport.write(b'%P$')
                if(g_serialport.in_waiting > 0):
                    GlobalVars.g_serial_port_rx_data = g_serialport.read(g_serialport.in_waiting)
                    print("data :" + str(GlobalVars.g_serial_port_rx_data))
                    l_sop = GlobalVars.g_serial_port_rx_data.find(b'%A$')
                    if(l_sop != -1):
                         GlobalVars.g_serial_port_connect_flag = True
                         print("Serial Port Connected Successfully")
                         break
                    else:
                        g_serialport.close()
                        print("Serial Port Closed-1")
                else:
                    g_serialport.close()
                    print("Serial Port Closed-2")
            else:     
                print("Port in use")            
        except:
            print("Exception in opening port " + port)
    
   

    if(GlobalVars.g_serial_port_connect_flag == True):
        g_serialport.write(b'hello')

    #foo()

    #while True:
    #    time.sleep(10.00)
    #    print("In while : " + str(time.ctime()))


    


        
    
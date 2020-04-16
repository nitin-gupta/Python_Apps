import sys
import threading
import time, datetime
from threading import Event, Thread

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
    
def func_square(l_val):
    l_square_val = l_val * l_val
    return l_square_val

def func_cube(l_val):
    l_cube_val = l_val * l_val * l_val
    return l_cube_val

def func_exponential(l_val, l_power):
    l_exp_val = pow(l_val,l_power)
    return l_exp_val

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
import time, threading

WAIT_SECONDS = 1
def test():
    print(time.ctime())
def foo():
    test()
    threading.Timer(WAIT_SECONDS, foo).start()
    
#foo()
threading.Timer(WAIT_SECONDS, foo).start()

while True:
    time.sleep(1)
    print("In while : " + str(time.ctime()))
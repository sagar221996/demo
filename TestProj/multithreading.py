'''
Created on 12-Mar-2020

@author: sgatla
'''
from threading import *
from time import sleep


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(i)
        
class Hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(i)
        
t1=Hello()
t2=Hi()

t1.start()
t2.start()

t1.join()       #it will tell main thread to wait
t2.join()

print("bye")                    #printed by main thread
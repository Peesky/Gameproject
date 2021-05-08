import socket
import pickle
import time
from build import *
import threading


"""
class bullet():
    def __init__(self,x,y):
        self.adresse = "IMG/equipe_R/bullet.png"
        self.imgsize = (20,20)
        self.x=x
        self.y=y
        self.life=3
        self.thr=threading.Thread(target=self.alive, args=())
        self.thr.start()

    def alive(self):
        while True:
            if self.life>0:
                self.life-=1
                time.sleep(0.5)
                print(self.life)
        print("ok, dead")

f=[]
for i in range(5):
    f.append(bullet(50,50))
print(f)"""

def pri():
    print("jojooooooooojo")

a = ["a",pri,"e","r","t","y"]
b=["aa","zz","ee","rr","tt","yy"]
c=["u","i","o","p"]
d=[a,b,c]
print(d[0][0])
d[0][1]()


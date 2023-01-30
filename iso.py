

#import upip
#upip.install('urequests')


import urequests

print("Versio=1")


import time,machine

from machine import TouchPad,Pin

outti=Pin(12,Pin.OUT)
led=Pin(2,Pin.OUT)
led2=Pin(13,Pin.OUT)
A=Pin(19,Pin.OUT)
B=Pin(21,Pin.OUT)
C=Pin(22,Pin.OUT)
D=Pin(23,Pin.OUT)

XT=TouchPad(Pin(4))
X0=TouchPad(Pin(14))

def tats(x):
    A.value(x&1)
    B.value((x>>1)&1)
    C.value((x>>2)&1)
    D.value((x>>3)&1)
    time.sleep(0.03)
    return XT.read()< 45 

if tats(3): exit

def touch():
    led2.value(1)
    while True:
        if X0.read()<500: return 100
        for x in range(16):
            if tats(x):
                led2.value(0)
                cou=0
                while tats(x) and cou<32: cou+=1
                if cou>30: return x+20
                else: return x

                    
NAPIT=[[7, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
[1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
[2, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
[3, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
[4, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0],
[5, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1],
[6, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1]]

                
kamala=10
def sendpulse(x):
    iik=0
    outti.value(1)
    for z in range(50): iik+=1
    outti.value(0)
    if x==0:
        for z in range(60): iik+=1
    elif x==1:
        for z in range(5*60): iik+=1
    elif x==2:
        for z in range(kamala*60): iik+=1
        
        
def send2(x):
    global NAPIT
    for y in NAPIT:
        if y[0]==x:
            sendpulse(2)
            sendpulse(0)
            sendpulse(1)
            sendpulse(1)
            for zuu in range(4):
                sendpulse(0)
                sendpulse(1)
            for z in y[1:]:
                sendpulse(z)
            sendpulse(1)
            
def send(x):
    for z in range(6):
        send2(x)
        time.sleep(0.01)
    time.sleep(1)

def urequ(x):
    led.value(1)
    print(x)
    try: urequests.get(x)
    except: pass
    led.value(0)


def all_off():
    led2.value(0)
    send(1)
    send(3)
    send(5)
    for x in range(4): urequ('http://192.168.1.65/r%soff'%(x+1))
    urequ('http://192.168.1.64/5/off')
    urequ('http://192.168.1.62/5/off')

            
def test():
    while True:
        for x in range(16):
            tu=touch()
            print(tu)
            if tu==0: send(2)
            elif tu==20: send(1)
            elif tu==1: send(4)
            elif tu==21: send(3)
            elif tu==2: send(6)
            elif tu==22: send(5)
            elif tu>3 and tu<8: urequ('http://192.168.1.65/r%son'%(tu-3))
            elif tu>23 and tu<28: urequ('http://192.168.1.65/r%soff'%(tu-23)) 
            elif tu>7 and tu<12: urequ('http://192.168.1.11:8083/ON%s'%(tu-7))
            elif tu>27 and tu<32: urequ('http://192.168.1.11:8083/OFF%s'%(tu-27))
            elif tu==12: urequ('http://192.168.1.64/5/on')
            elif tu==32: urequ('http://192.168.1.64/5/off')
            elif tu==13: urequ('http://192.168.1.62/5/on')
            elif tu==33: urequ('http://192.168.1.62/5/off')
            elif tu==35:
                led2.value(0)
                machine.reset()
            elif tu==100:
                cou=0
                while X0.read()<500 and cou<25:
                    time.sleep(0.1)
                    cou+=1
                if cou>20: all_off()
            else: time.sleep(0.3)
            if tu in range(20,50): time.sleep(2)
test()

        

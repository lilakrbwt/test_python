from microbit import *
from maqueen import Maqueen
from microbit import *
import radio
import utime


radio.on()
radio.config(group=9)

VITESSE = 35
VITESSE_LENTE = 11
STOP = 0

robot = Maqueen()



def Avance():
    robot.motor_left(VITESSE)
    robot.motor_right(VITESSE)
    
def Recule():
    robot.motor_left(VITESSE,1)
    robot.motor_right(VITESSE,1)

def Gauche():
    robot.motor_right(VITESSE_LENTE)
    robot.motor_left(VITESSE)

def Droite():
    robot.motor_left(VITESSE_LENTE)
    robot.motor_right(VITESSE)

def Stop():
    robot.motor_left(STOP)
    robot.motor_right(STOP)
    
    
while True:
    msg=radio.receive()
    print(msg)
    if msg is not None:
        print(msg)
        if msg == "avance":
            Avance()
        
        elif msg == "recule":
            Recule()
        
        elif msg == "gauche":
            Gauche()
            
        elif msg == "droite":
            Droite()
        
        elif msg == "stop":
            Stop()
    sleep(200)

    

    
    
        
        
        
        
        
    
    
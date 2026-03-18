""" Auteurs		: Lila Karyabwite, Milo Gumprecht
    Contact		: lila.krbwt@eduge.ch, milo.gmprc@eduge.ch
    Date		: 18 février 2026
    Version		: 1.0
    Description	: Code du robot, permet de fonctionner en fonction des commandes envoyé par le joystick avec la radio
"""

# importer les librairies
from microbit import *
from maqueen import Maqueen
from microbit import *
import radio




# allumer radio
radio.on()

# canal propre au groupe
radio.config(group=9)

# definition des variables
VITESSE = 35
VITESSE_LENTE = 11
STOP = 0

robot = Maqueen()


# fonctions pour les directions du robot et la fete
def Avance():
    robot.motor_left(VITESSE)
    robot.motor_right(VITESSE)
    
    
def Recule():
    robot.motor_left(VITESSE,1)
    robot.motor_right(VITESSE,1)

def Gauche():
    robot.motor_left(VITESSE_LENTE)
    robot.motor_right(VITESSE)

def Droite():
    robot.motor_right(VITESSE_LENTE)
    robot.motor_left(VITESSE)

def Stop():
    robot.motor_left(STOP)
    robot.motor_right(STOP)


while True:
#     recevoir le message
    msg=radio.receive()

# boucle pour eviter les None
    if msg is not None:
        print(msg)
        
#robot avance 
        if msg == "avance":
            Avance()
# robot recule
        elif msg == "recule":
            Recule()
        
# robot va a gauche
        elif msg == "gauche":
            Gauche()
            
# robot va a droite
        elif msg == "droite":
            Droite()
            
# robot s'arrete 
        elif msg == "stop":
            Stop()
            
    
    sleep(30)

    

    
    
        
        
        
        
        
    
    
""" Auteurs		: Lila Karyabwite, Milo Gumprecht
    Contact		: lila.krbwt@eduge.ch, milo.gmprc@eduge.ch
    License		: MILA_LILO
    Date		: 18 mars 2026
    Version		: 1.0
    Description	: Code du joystick, permet d'envoyer les messages, avec la radio, par rapport au valeurs rapporter par le joystick
"""

# importer les librairies
from microbit import*
import radio

# allumer la radio
radio.on()

# canal propre au groupe 
radio.config(group=9)

  
    
while True:
# variables pour les differentes valeurs
    x = pin1.read_analog()
    y = pin0.read_analog()
    z = pin2.read_digital()
    
# joystick vers le haut
    if y>=600:
        radio.send("avance")

# joystick vers le bas
    elif y<=100:
        radio.send("recule")

# joystick vers la droite
    elif x>=800:
        radio.send("droite")
   
# joystick vers la gauche
    elif x<=300:
        radio.send("gauche")
        
 
# arret si dans zone morte 
    else:
        radio.send("stop")
    
    sleep(30)
         

    


    

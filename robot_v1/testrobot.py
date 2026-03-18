# Librairie   : https://github.com/kholm777/maqueen/tree/main
from maqueen import Maqueen
from microbit import * 
import utime

# Constantes
WHITE = 1
BLACK = 0

VITESSE = 35
VITESSE_LENTE = 11
STOP = 0
robot = Maqueen()
display.show(Image.HAPPY)
# robot.motor_left(200,1)
# utime.sleep_ms(2000)
def obstacle_detected():
    #utime.sleep_ms(50)
    return(1 < robot.ultrasound_measure() < 8)

while True:
    
    if obstacle_detected():
        robot.motor_left(VITESSE,1)
        robot.motor_right(VITESSE,1)
        sleep(500)
        robot.motor_left(VITESSE_LENTE)
        robot.motor_right(VITESSE)
        sleep(200)
        robot.motor_left(VITESSE)
        robot.motor_right(VITESSE)
#         sleep(500)
#         robot.motor_left(VITESSE)
#         robot.motor_right(VITESSE_LENTE)

        robot.rgb_front_left(255,0,0)
        robot.rgb_front_right(255,0,0)
        robot.rgb_rear_left(255,0,0)
        robot.rgb_rear_right(255,0,0)
        robot.led_left(1)
        
    elif robot.line_left()==BLACK and robot.line_right()==BLACK: 
        robot.motor_left(VITESSE)
        robot.motor_right(VITESSE)
        robot.rgb_front_left(255,0,255)
        robot.rgb_front_right(255,0,255)
        robot.rgb_rear_left(255,0,255)
        robot.rgb_rear_right(255,0,255)
#         sleep(1000)
    elif robot.line_left()==WHITE and robot.line_right()==BLACK:
        robot.motor_right(VITESSE_LENTE)
        robot.motor_left(VITESSE)
        robot.rgb_front_left(0,255,0)
        robot.rgb_front_right(0,255,0)
        robot.rgb_rear_left(0,255,0)
        robot.rgb_rear_right(0,255,0)
#         sleep(1000)
    elif robot.line_left()==BLACK and robot.line_right()==WHITE:
        robot.motor_left(VITESSE_LENTE)
        robot.motor_right(VITESSE)
        robot.rgb_front_left(0,0,255)
        robot.rgb_front_right(0,0,255)
        robot.rgb_rear_left(0,0,255)
        robot.rgb_rear_right(0,0,255)
    utime.sleep_ms(30)
    
from microbit import *
while True:
    print("X=",pin1.read_analog())
    print("Y=",pin0.read_analog())
    if pin2.read_digital() == 1:
        print("Z pressed")
    sleep(200)
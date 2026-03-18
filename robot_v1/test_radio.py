import radio
from microbit import display, button_a, button_b, sleep

radio.on()
radio.config(group=9)

def send_txt(text):
    radio.send("TXT:" + text)

while True:
    if button_a.was_pressed():
        send_txt("salut")
    if button_b.was_pressed():
        send_txt("ca va?")
    msg = radio.receive()
    if msg is not None and msg.startswith("TXT:"):
        display.scroll(msg[4:]) # on retire "TXT:"
    sleep(50)
from flask import Flask
from gpiozero import LED, Button

red_led = LED(18)
green_led = LED(15)

button = Button(14)

while True:
    if button.is_pressed:
        print("order processed")
        green_led.on()
    else:
        red_led.on()
        green_led.off()



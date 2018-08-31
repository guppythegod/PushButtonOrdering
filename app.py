from flask import Flask
from gpiozero import LED, button
import firebase_admin
import os

red_led = LED(18)
green_led = LED(15)

button = button(14)

if button.is_pressed = red_led.on()



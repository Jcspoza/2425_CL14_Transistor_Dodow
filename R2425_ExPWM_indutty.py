# Taller Programación y Robótica en CMM BML – 2024-2025 - Dodow
# Programa: Dodow version 1 - respiracion lineal en 100 pasos
# Hardware platform: Pico _ & W / funciona igual sin cambios
# Librerias : Ninguna
# Ref librerias: 
# Fecha JCSP 2025 06
# Licencia : CC BY-NC-SA 4.0
# REf basica https://dmccreary.github.io/learning-micropython/basics/04-fade-in-and-out/

from machine import Pin, PWM
from utime import sleep

# Informative block - start
p_ucontroler = "Pico W"
p_keyOhw = "Led + resistor on GPIO15"
p_project = "External LED - PWM input - 1000Hz"
p_version = "1.0"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

EXTERNAL_LED_PIN = 15
pwm_led = PWM(Pin(EXTERNAL_LED_PIN))
pwm_led.freq(1000)

por60mil = 32500
try:
    while (True):
        pwm_led.duty_u16(por60mil)
        pm = input("Por 60mil (0 a 65000)= ")
        por60mil = int(pm)
        
except KeyboardInterrupt:
    pwm_led.duty_u16(0)
    pwm_led.deinit()
        

# Taller Programación y Robótica en CMM BML – 2024-2025 - Dodow
# Programa: Dodow version 2 - respiracion lineal todos ciclos
# Hardware platform: Pico _ & W / funciona igual sin cambios
# Librerias : Ninguna
# Ref librerias: 
# Fecha JCSP 2025 06
# Licencia : CC BY-NC-SA 4.0
# REf basica https://www.coderdojotc.org/micropython/basics/04-fade-in-and-out/

from os import uname
# Informative block - start
p_project = "Dodow PWM - Importa Respiracion"
p_keyOhw = "Blue LED 1w & NPN s8050 in GPIO15"
p_version = "2.0"
p_library = "none"
print(f"uPython version: {uname()[3]} ")
print(f"uC: {uname()[4]} - Key other HW: {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
print(f"Key Library: {p_library}")
# Informative block - end

# 0-Imports
from machine import Pin, PWM
from utime import sleep_ms
from FuncRespL1ms2_0 import respiraL1ms as respiraLed # immporta respiraLed

# 1- Constants & global variables
EXT_LED_PIN = 15
MINPWM = 500
MAXPWM = 65500
RANPWM = (MAXPWM - MINPWM)
DEBUG = True
SEC8MIN = ((11,1),(10,1),(9,1),(8,1),(7,1),(6,3))
SEC20MIN = ((11,3),(10,3),(9,3),(8,3),(7,3),(6,5))

# 2- Creacion d eobjetos e inicializacion
pwmLed = PWM(Pin(EXT_LED_PIN))
pwmLed.freq(1000)
pwmLed.duty_u16(MINPWM)


# 1- Inicio de programa
tipoSecuencia = ''
while tipoSecuencia != 'c' and tipoSecuencia != 'l':
    tipoSecuencia = input('Tipo de secuencia 8(c) o 20 (l) minutos ')[0].lower()
try:
    if tipoSecuencia == 'c':
        for ciclo in range(len(SEC8MIN)):
            durarepsactualms = 60_000 // SEC8MIN[ciclo][0]
            totalResp = SEC8MIN[ciclo][0] * SEC8MIN[ciclo][1]
            if DEBUG:   
                print(f'Secuencia {tipoSecuencia}, Cada resp={durarepsactualms} ms/ RxM={SEC8MIN[ciclo][0]} / Total resp={totalResp} ')
                
            for nresp in range(totalResp):
                if DEBUG:   
                    print('Resp # ',nresp)
                    
                TipResp = respiraLed(pwmLed, durarepsactualms)
                if DEBUG:   
                    print('Tipo de respiracion ', TipResp)

    if tipoSecuencia == 'l':
        for ciclo in range(len(SEC20MIN)):
            durarepsactualms = 60_000 // SEC20MIN[ciclo][0]
            totalResp = SEC8MIN[ciclo][0] * SEC20MIN[ciclo][1]
            if DEBUG:
                print(f'Secuencia {tipoSecuencia}, Cada resp={durarepsactualms} ms/ RxM={SEC20MIN[ciclo][0]} / Total resp={totalResp} ')
                            
            for nresp in range(totalResp):
                if DEBUG:   
                    print('Resp # ',nresp)
                    
                TipResp = respiraLed(pwmLed, durarepsactualms)
                if DEBUG:   
                    print('Tipo de respiracion ', TipResp)

except KeyboardInterrupt:
    pwmLed.duty_u16(0)
    pwmLed.deinit() 

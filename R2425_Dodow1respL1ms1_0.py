# Taller Programación y Robótica en CMM BML – 2024-2025 - Dodow
# Programa: Dodow version 1 - respiracion lineal
# Hardware platform: Pico _ & W / funciona igual sin cambios
# Librerias : Ninguna
# Ref librerias: 
# Fecha JCSP 2025 06
# Licencia : CC BY-NC-SA 4.0
# REf basica https://dmccreary.github.io/learning-micropython/basics/04-fade-in-and-out/

from os import uname
# Informative block - start
p_project = "Dodow PWM - 1 respiracion lineal paso 1ms"
p_keyOhw = "Blue LED 1w & NPN s8050 in GPIO15"
p_version = "1.0"
p_library = "none"
print(f"uPython version: {uname()[3]} ")
print(f"uC: {uname()[4]} - Key other HW: {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
print(f"Key Library: {p_library}")
# Informative block - end

# 0-Imports
from machine import Pin, PWM
from utime import sleep_ms

# 1- Constants & global variables
EXT_LED_PIN = 15
MINPWM = 500
MAXPWM = 65500
RANPWM = (MAXPWM - MINPWM)
DEBUG = True

pwmLed = PWM(Pin(EXT_LED_PIN))
pwmLed.freq(1000)

def respiraL1ms(pinpwm , duracionrespms, debug = False):
    """ Realiza una respiracion = subir luz led + bajar led - curvas lineales
        
        Detalles : La respiracion se divide en 3/10 inspiracion + 6/10 expiracion
        + 1/10 en el minimo de luz. Tanto la curva de subida como de bajda son lineales
        desde MINPWM a MAXPWM y viceversa. Esto tiene un problema perceptivo porque
        el ojo lo ve como subida logaritmica (ver otro programa respiraExp que compensa)
        
        Parametros
           - pinpwm : el pin donde esta conectado el led , objeto PWM ya creado
           - duracionrespms : duracion de un arespiracion insp+expira complete en milisegundos
           - debug : true da mensajes dedebug
    """
    decimams = duracionrespms // 10
    inspirams = decimams * 3
    expirams = decimams * 6
    reposo = decimams
    inspiraPaso = RANPWM // inspirams
    expiraPaso = RANPWM // expirams
    pinpwm.duty_u16(MINPWM)
    
    if debug:          
        print('Inicio duty_u16 =',pinpwm.duty_u16()) # debug
        print(f'Inspira incre x ms {inspiraPaso} x dura ms {inspirams}') 
    
    for p in range(inspirams+1):
        pinpwm.duty_u16(MINPWM + p * inspiraPaso)
        sleep_ms(1)
    
    if debug:   
        print('Fin up duty_u16 =',pinpwm.duty_u16(), 'Ultimo paso=', p) # debug
        print(f'Expira decre x ms {expiraPaso} x dura ms {expirams}') 
    for p in range(expirams+1):
        pinpwm.duty_u16(MAXPWM - p * expiraPaso)
        sleep_ms(1)
    
    if debug:    
        print('Fin down duty_u16 =',pinpwm.duty_u16(),'Ultimo paso=', p) # debug
        print(f'Reposo dura ms {decimams}') 
        
    pinpwm.duty_u16(MINPWM)
    sleep_ms(decimams)
    
    if debug:
        print('Fin resp duty_u16 =',pinpwm.duty_u16()) # debug


durarepsactualms = 60_000 // 10 # 10 respiraciones por minuto
respiraL1ms(pwmLed, durarepsactualms, DEBUG)

pwmLed.duty_u16(0)
pwmLed.deinit() 

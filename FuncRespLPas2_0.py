# Taller Programación y Robótica en CMM BML – 2024-2025 - Dodow
# Programa: Dodow version 1 - respiracion lineal
# Hardware platform: Pico _ & W / funciona igual sin cambios
# Librerias : Ninguna
# Ref librerias: 
# Fecha JCSP 2025 06
# Licencia : CC BY-NC-SA 4.0
# REf basica https://dmccreary.github.io/learning-micropython/basics/04-fade-in-and-out/
# 1.0 -> 2.0 poner en modo importable

# Informative block - start
p_project = "Dodow PWM - Funccion Respiracion lineal en 500 pasos"
p_version = "2.0"
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

# 0-Imports
from machine import Pin, PWM
from utime import sleep

# 1- Constants & global variables
MINPWM = 500
MAXPWM = 65500
RANPWM = (MAXPWM - MINPWM)
PASOS = 500
PASOPWM = RANPWM // PASOS

def respiraLPas(pinpwm , duracionrespms, debug = False):
    """ Realiza una respiracion = subir luz led + bajar led - curvas lineales 500 pasos
        
        Detalles : La respiracion se divide en 4/10 inspiracion + 5/10 expiracion
        + 1/10 en el minimo de luz. Tanto la curva de subida como de bajda son lineales
        desde MINPWM a MAXPWM y viceversa. Esto tiene un problema perceptivo porque
        el ojo lo ve como subida logaritmica (ver otro programa respiraExp que compensa)
        
        Parametros
           - pinpwm : el pin donde esta conectado el led , objeto PWM ya creado
           - duracionrespms : duracion de un arespiracion insp+expira complete en milisegundos
           - debug : true da mensajes dedebug
    """
        
    decimams = duracionrespms / 10
    inspirams = decimams * 4
    expirams = decimams * 5
    reposo = decimams
    insPasoms = inspirams / PASOS
    expPasoms = expirams / PASOS
    pinpwm.duty_u16(MINPWM)
    
    if debug:
        print(f'PasoPWM {PASOPWM} x {PASOS} = {PASOPWM * PASOS}') 
        print('Inicio duty_u16 =',pinpwm.duty_u16()) # debug
        print(f'Inspira duracion: paso ms {insPasoms}, tot {insPasoms*PASOS}') 
    
    for p in range(PASOS):
        pinpwm.duty_u16(MINPWM + p * PASOPWM)
        sleep(insPasoms/1000)
    
    if debug:   
        print('Fin up duty_u16 =',pinpwm.duty_u16(), p) # debug
        print(f'Expira duracion: paso ms {expPasoms}, tot {expPasoms*PASOS}') 
        
    for p in range(PASOS):
        pinpwm.duty_u16(MAXPWM - p * PASOPWM)
        sleep(expPasoms/1000)
    
    if debug:    
        print('Fin down duty_u16 =',pinpwm.duty_u16(),p) # debug
        
    pinpwm.duty_u16(MINPWM)
    sleep(decimams/1000)
    
    if debug:
        print(f'Resposo duracion ms {decimams}') 
        print('Fin resp duty_u16 =',pinpwm.duty_u16()) # debug
    
        
    return 'Respiracion Lineal 4_5_1 - 500 pasos'

# F- Fin funciones

if (__name__ == '__main__'):
    EXT_LED_PIN = 15
    DEBUG = True
    
    pwmLed = PWM(Pin(EXT_LED_PIN))
    pwmLed.freq(1000)
    pwmLed.duty_u16(MINPWM)
    
    durarepsactualms = 60_000 // 10 # 10 respiraciones por minuto
    print('Tipo =',respiraLPas(pwmLed, durarepsactualms, DEBUG))

    pwmLed.duty_u16(0)
    pwmLed.deinit() 

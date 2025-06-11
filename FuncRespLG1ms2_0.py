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
p_project = "Dodow PWM - Funccion Respiracion lineal paso 1ms- Gamma correccion"
p_version = "2.0"
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

# 0-Imports
from machine import Pin, PWM
from utime import sleep_ms

# 1- Constants & global variables
MINPWM = 500
MAXPWM = 65500
RANPWM = (MAXPWM - MINPWM)

def respiraLG1ms(pinpwm , duracionrespms, debug = False):
    """ Realiza una respiracion = subir luz led + bajar led - curvas lineales- Corr Gamma
        
        Detalles : La respiracion se divide en 3/10 inspiracion + 6/10 expiracion
        + 1/10 en el minimo de luz. Correccion Gamma compensa la precepcion logaritmica
        
        Parametros
           - pinpwm : el pin donde esta conectado el led , objeto PWM ya creado
           - duracionrespms : duracion de un arespiracion insp+expira complete en milisegundos
           - debug : true da mensajes dedebug
    """
    def gamma(lin):
        """Convierte un valor lineal entre 0.0 y 1.0 en corregido gamma"""
    
        if lin < 0.0:
            return 0.0
        elif lin > 1.0:
            return 1.0
        else:
            return lin ** 2.2
    
    
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
        # correccion  gamma
        pinpwm.duty_u16(MINPWM + int(gamma((p*inspiraPaso)/RANPWM)*RANPWM))
        sleep_ms(1)
    
    if debug:   
        print('Fin up duty_u16 =',pinpwm.duty_u16(), 'Ultimo paso=', p) # debug
        print(f'Expira decre x ms {expiraPaso} x dura ms {expirams}') 
    for p in range(expirams+1):
        # correcion gamma
        pinpwm.duty_u16(MAXPWM - int(gamma((p*expiraPaso)/RANPWM)*RANPWM))
        sleep_ms(1)
    
    if debug:    
        print('Fin down duty_u16 =',pinpwm.duty_u16(),'Ultimo paso=', p) # debug
        print(f'Reposo dura ms {decimams}') 
        
    pinpwm.duty_u16(MINPWM)
    sleep_ms(decimams)
    
    if debug:
        print('Fin resp duty_u16 =',pinpwm.duty_u16()) # debug
        
    return 'Respiracion Lineal 3_6_1- paso 1ms - Corregido Gamma'

# F- Fin funciones

if (__name__ == '__main__'):
    EXT_LED_PIN = 15
    DEBUG = True
    
    pwmLed = PWM(Pin(EXT_LED_PIN))
    pwmLed.freq(1000)
    pwmLed.duty_u16(MINPWM)
    
    durarepsactualms = 60_000 // 10 # 10 respiraciones por minuto
    print('Tipo =',respiraLG1ms(pwmLed, durarepsactualms, DEBUG))

    pwmLed.duty_u16(0)
    pwmLed.deinit() 

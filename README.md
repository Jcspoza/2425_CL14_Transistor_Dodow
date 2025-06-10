# CL14-uP: Transistor y Proyecto Dodow sueño >draft<

Forma parte de la serie '**Workshop about Python and micropython with Pico W in CMM Benito**' Martin Madrid

## Clase 14 - Indice - 90 minutos

- 0.Objetivo

- 1.Tutoriales, Programas, Conexionado y Librerias

- 2.Entender circuito de transistor

- 3.Proyecto Dodow - ayuda para el sueño

## 0. Objetivo

Para acabar el curso un pequeño proyecto que se puede continuar en vacaciones:

Vamos a hacer un prototipo de un aparato que ayuda a conciliar el sueño , 'Dodow' : se trata de sincronizar la respiración con la luz de un led pulsante. La idea es ir bajando de ritmo de la pulsación de luz desde 11 ciclos por minuto  (subir brillo = inspiración-> bajar brillo = expiracion)  a 6 ciclos por minuto. El aparato comercial tiene dos secuencias :

- Larga 20 minutos desde las 11 respiraciones pro minuto a las 6 respiraciones

- Corta de 8 minutos también desde 11 a 6 respiraciones por minuto

[Dodow web oficial | Duérmete más rápido | Pruébalo 100 días](https://www.mydodow.com/dodow/es-es/bundles)

[Dodow : découvrez comment il va vous endormir. - YouTube](https://youtu.be/kY5L8FCDVtc)

Como se ve, el Dodow comercial usa un luz azul pulsante. Vamos a necesitar un led azul de potencia de 1w . Para controlarlo usaremos PWM cambando esta vez el ciclo de trabajo (No la frecuencia), pero necesitamos bastantes miliamperios (+ de 100 mA ) con lo que usaremso un circuito de transistor

## 1. Tutoriales, Programas que vamos a usar y conexionado

### Tutoriales resumen

**PWM y led**

[Fade In and Out - Learning MicroPython](https://dmccreary.github.io/learning-micropython/basics/04-fade-in-and-out/)

Del **Dodow do it yourself**  hay tutoriales, pero para leguaje arduino

-     [DIY Dodow Clone Arduino Sleep Meditation Machine : 4 Steps (with Pictures) - Instructables](https://www.instructables.com/DIY-Dodow-Clone-Arduino-Sleep-Meditation-Machine/)

-     [GitHub - dshiffman/dodowDIY: An ATTiny85 implementation of the well known sleep aid. Includes circuit, software and 3d printed case design](https://github.com/dshiffman/dodowDIY/tree/main)

Del **transistor BJC**: 

- un buen tutorial [Transistor bipolar BJT y Arduino](https://programarfacil.com/blog/arduino-blog/transistor-bipolar-bjt-npn/)

- Del libro Electrónica para makers Guía completa' de Paolo Aliverti, leer el capitulo 'El transistor bipolar'

- El tutorial de sunfounder sobre transistores NO es muy bueno
  
  [Transistor — SunFounder Kepler Kit for Raspberry Pi Pico W 1.0 documentation](https://docs.sunfounder.com/projects/kepler-kit/en/latest/component/component_transistor.html)

----

### Tabla resumen de programas

Ningún programa necesita hw adicional

| Programa                                         | Lenguaje | Objetivo de Aprendizaje         |
| ------------------------------------------------ | -------- | ------------------------------- |
| [R2425_ExPWM_indutty.py](R2425_ExPWM_indutty.py) | uPy      | Test básico de PWM y conexiones |
|                                                  |          |                                 |
|                                                  |          |                                 |
|                                                  |          |                                 |
|                                                  |          |                                 |

### 

## Conexionado circuito test de transistor

![](C:\Users\josec\OneDrive\Documentos\GitHub\2425_CL14_Transistor_Dodow\test_tnpn_led1w_esquemático.png)

### Conexionado circuito Dodow

Es muy parecido al conexionado de la CL13 sonido. de nuevo el elemento d epotencia se alimenta a +5vol del usb

TODO : comentar como seri aun alimentación autónoma

![](./picow_tnpn_led1w_bb.png)

### Librerias

No usaremos ninguna libreria.

## 2. Entender el circuito de transistor

Un buen tutorial para entender el uso de transistores BJC en modo corte-saturación es

[Transistor bipolar BJT y Arduino](https://programarfacil.com/blog/arduino-blog/transistor-bipolar-bjt-npn/)

o leer el capitulo 'El transistor bipolar' del libro 'Electrónica para makers Guía completa' de Paolo Aliverti

Vamos a medir voltajes y corrientes en distintas partes del circuito, especialmente corrientes en el circuito de base-emisor y el de emisor-colector-led

![](C:\Users\josec\OneDrive\Documentos\GitHub\2425_CL14_Transistor_Dodow\test_tnpn_led1w_esquemáticoAmp.png)

Estos son algunos valores reales hallados por mi.  Cuidado he usado un transistor2n2222A porque tengo mas de estos !!! De la hoja de datos

Vbe = 0.6 a 1.2 volt

Vce = 0.3 a 1.0 volt

==> Haz el montaje y mide los valores

APRENDIZAJES:

* Cuando necesitamos controlar dispositivos que consumen > 20mA este montaje de transisitor en corte-saturación es muy util

* Se pueden controlar con la Pico ( lógica a 3,3 volt) dispositivos con mucho mas voltaje, usando este montaje de transistor BJC en corte - saturación

## 3.Proyecto Dodow - ayuda para el sueño

Una vez que hemos resuelto el problema del HW : 

    Ya sabemos como **dar mucha corriente a un Led azul de potencia** que puede llegar a consumir unos 300mA ( en realidad consume unos 120 mA), 

hay que ver como abordar el proyecto Sw de micropython. Veo estas partes 

1. Sabemos como cambiar la luz del led usando el ciclo de trabajo de un pulso PWM
   
   1. Necesitamos un programa de test

2. **Ciclo de respiración** = subir la luz del del y luego bajar = > HACER
   
   1. Probemos con 10 respiraciones por minuto
   2. Subida y bajada lineal + un reposo : 3 + 6 +1 por ejemplo x 2 posibilidades
      1. por cambio cada 1msegundo
      2. por numero fijo de pasos

3. **Secuencia de respiraciones** => HACER
   
   1. dos bucles for

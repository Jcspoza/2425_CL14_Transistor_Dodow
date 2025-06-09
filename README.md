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

Del Dodow do it yourself hay tutoriales, pero para leguaje arduino

[DIY Dodow Clone Arduino Sleep Meditation Machine : 4 Steps (with Pictures) - Instructables](https://www.instructables.com/DIY-Dodow-Clone-Arduino-Sleep-Meditation-Machine/)

[GitHub - dshiffman/dodowDIY: An ATTiny85 implementation of the well known sleep aid. Includes circuit, software and 3d printed case design](https://github.com/dshiffman/dodowDIY/tree/main)

De **Sunfounder** tutorial del transistor : 

----

### Tabla resumen de programas

| Programa | Lenguaje | Objetivo de Aprendizaje | Hw adicional |
| -------- | -------- | ----------------------- | ------------ |
|          |          |                         |              |
|          |          |                         |              |
|          |          |                         |              |
|          |          |                         |              |
|          |          |                         |              |
|          |          |                         |              |
|          |          |                         |              |
|          |          |                         |              |
|          |          |                         |              |
|          |          |                         |              |

### Conexionado

Es muy parecido al conexionado de la CL13 sonido. de nuevo el elemento d epotencia se alimenta a +5vol del usb

TODO : comentar como seri aun alimentación autónoma

![](C:\Users\josec\OneDrive\Documentos\GitHub\2425_CL14_Transistor_Dodow\picow_tnpn_led1w_bb.png)

### Libreria

No usaremos ninguna libreria.

## 2. Entender el circuito de transistor

Un buen tutorial para entender el uso de transistores BJC en modo corte-saturación es

[Transistor bipolar BJT y Arduino](https://programarfacil.com/blog/arduino-blog/transistor-bipolar-bjt-npn/)

o leer el capitulo 'El transistor bipolar' del libro 'Electrónica para makers Guía completa' de Paolo Aliverti

El tutorial de sunfounder sobre transistores NO es muy bueno

[Transistor &mdash; SunFounder Kepler Kit for Raspberry Pi Pico W 1.0 documentation](https://docs.sunfounder.com/projects/kepler-kit/en/latest/component/component_transistor.html)

## Preguntas sobre la Clase 14 - 10 minutos

Sección para que los alumnos pregunten sus dudas durante la clase

---

## TO DO :

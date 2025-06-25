# Workshop 3 - Spacecraft Systems Simulation

**Autores:**  
- Santiago Flórez  
- David Arévalo  
- Juan Pablo Rincón  
- Schneider Alejandro Torres  

## Descripción del Proyecto
Este proyecto simula el comportamiento básico de una nave espacial en órbita usando principios de Programación Orientada a Objetos (OOP). La simulación incluye el control de actitud (orientación), el sistema de energía, la carga útil (cámara), la comunicación con la Tierra y eventos externos como eclipses.

El objetivo es observar cómo interactúan estos subsistemas y cómo responden a condiciones cambiantes del entorno como la presencia o ausencia de luz solar.

## ¿Qué hace el código?

- La nave tiene orientación que cambia con el tiempo.
- Tiene un sistema de energía que se carga con luz solar y se descarga en eclipses.
- Si hay eclipse, no entra energía, y el sistema se descarga rápidamente.
- La batería se carga +5 por iteración con sol y se descarga -10 sin él.
- Si la batería baja de 20%, la nave ya no puede transmitir datos a la Tierra.
- La carga útil es una cámara que aumenta su temperatura en cada captura.
- Se simula el paso del tiempo con un `for` de 20 iteraciones por defecto.
- Los sistemas están encapsulados mediante `getters` y `setters` para evitar acceso directo a los atributos internos.

## Diseño Orientado a Objetos

El programa está estructurado con varias clases que representan los subsistemas de la nave:

- **BaseSystem (abstracta):** Superclase base para todos los subsistemas que define el método `update()`.
- **AttitudeControlSystem:** Maneja la orientación de la nave en grados (0° a 359°).
- **PowerSystem:** Administra la batería y la entrada solar.
- **PayloadCamera:** Simula una cámara que toma imágenes y sube su temperatura.
- **CommSystem:** Permite transmitir datos si la batería no está baja.
- **EventManager:** Controla eventos externos como eclipses solares.
- **Ship:** Hereda y combina todos los sistemas anteriores y define su comportamiento global.
- **main():** Ejecuta la simulación durante 20 ciclos por defecto.

## Flujo de Ejecución

1. Se crea un objeto `Ship`.
2. En cada iteración (tiempo), se ejecuta:
   - Control de eventos (`EventManager`)
   - Actualización de orientación (`AttitudeControlSystem`)
   - Carga o descarga de batería (`PowerSystem`)
   - Activación de la cámara (`PayloadCamera`)
   - Comunicación con la Tierra si hay batería suficiente (`CommSystem`)

## Ejemplo resumido de Salida

```plaintext
--- Time Step ---
[Attitude] Orientation is now 1°
[Power] Charging from solar. Battery: 100%
[Payload] Capturing image at 21°C
[Comms] Transmitting data to Earth.

[Event] Eclipse started! Solar input disabled.
[Power] Discharging battery. Battery: 95%


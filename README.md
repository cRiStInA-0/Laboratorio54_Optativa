# Laboratorio: Control por voz de un robot industrial 4.0
## Objetivo:
Integrar reconocimiento de voz offline (Vosk) con Tkinter para controlar el panel de control de un robot industrial
4.0 de forma simulada.
## Comandos de ejemplo:
- “activar robot”
- “detener robot”
- “temperatura alta”
- “revisar sensores”
- “salir”
## Ejecutar:
```bash
python main.py
```

# Modificaciones realizadas para el laboratorio 54
Para esta ocasión, se pide implementar el laboratorio anteriormente realizado, pero agrregándole un sistema de autorización de voz.

## Instalación de dependencias
Para que todo funcione según lo previsto, hay que realizar las siguientes instalaciones:

- Microsoft C++ Build Tools (recomendado). Durante su instalación, hay que seleccionar la opción que dice “Desarrollo en Escritorio con C++”.

- Instalación de nuevas librerías.

```bash
pip install sounddevice numpy scipy librosa vosk matplotlib resemblyzer
```

## Instrucciones de uso
Para llevar a cabo este laboratorio, es necesario iniciar primero el archivo audio_autentification.py y seguir las indicaciones para obtener una muestra de voz y poder identificar si el usuario que utiliza la aplicación es el autorizado o no. 
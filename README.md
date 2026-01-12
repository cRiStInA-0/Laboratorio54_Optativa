# Modificaciones realizadas para el laboratorio 54
Para esta ocasión, se pide implementar el laboratorio anteriormente realizado (Laboratorio 53), pero agregándole un sistema de autorización de voz que permita identificar si el usuario tiene la autoridad para utilizar el sistema.

## Instalación de dependencias
Para que todo funcione según lo previsto, hay que realizar las siguientes instalaciones:

- Microsoft C++ Build Tools (recomendado). Durante su instalación, hay que seleccionar la opción que dice “Desarrollo en Escritorio con C++”.

- Instalación de nuevas librerías.

```bash
pip install sounddevice numpy scipy librosa vosk matplotlib resemblyzer
```
## Archivos modificados y/o agregados
- audio_manager.py
- command_processor.py
- main.py
- audio_autentification.py

## Instrucciones de uso
Para llevar a cabo este laboratorio, es necesario iniciar primero el archivo audio_autentification.py y seguir las indicaciones para obtener una muestra de voz y poder identificar si el usuario que utiliza la aplicación es el autorizado o no. 
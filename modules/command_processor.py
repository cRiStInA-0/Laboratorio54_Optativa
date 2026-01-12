from tkinter import messagebox

# Verificación con Resemblyzer (ejecutar localmente, requiere instalación)
from resemblyzer import VoiceEncoder, preprocess_wav
from scipy.spatial.distance import cosine
from pathlib import Path
import numpy as np

encoder = VoiceEncoder() #Inicializar encoder

def procesar_comando(text, audio, canvas, sensores, resultado_label, ventana):
 """
 Procesa el comando de voz y actualiza el semáforo tricolor.
 luces: tupla (temperatura, proximidad, energia) con los IDs de los óvalos en el canvas
 """
 temperatura, proximidad, energia = sensores
 text = text.lower() # Convertimos a minúsculas para evitar errores

 # RUTA: audio de perfil autorizado (graba previamente un archivo 'audio_autorizado.wav' con la voz permitida)
 perfil_path = Path("audio_autorizacion.wav")

 # Comprobar si el archivo de audio existe
 if not perfil_path.exists():
    resultado_label.config(text="ATENCIÓN: No se encontró 'audio_autorizacion.wav'. Crea este archivo con la voz autorizada para probar la verificación.", fg="orange")
    return
 
 perfil_wav = preprocess_wav(str(perfil_path))
 perfil_embedding = encoder.embed_utterance(perfil_wav)

 # Embedding del audio capturado
 audio_convertido = (audio.astype(np.float32) / 32768.0).flatten()
 capturado_wav = preprocess_wav(audio_convertido)
 capturado_embedding = encoder.embed_utterance(capturado_wav)

 # Comparar similitud
 similitud = 1 - cosine(perfil_embedding, capturado_embedding)
 print(f"Similitud con perfil autorizado: {similitud:.3f}")

 #Mediante el umbral se comprueba si la voz es autorizada o no
 UMBRAL = 0.75
 if similitud < UMBRAL:
    resultado_label.config(text="❌ Voz no autorizada. No puede utilizar el sistema.", fg="red")
 else:
   #Funciones if que busca similitud entre el texto y los "comandos"
   if "activar" in text and "robot" in text:
      #Se modifica el color de los canvas y la etiqueta
      canvas.itemconfig(temperatura, fill="green")
      canvas.itemconfig(proximidad, fill="green")
      canvas.itemconfig(energia, fill="green")
      resultado_label.config(text="🤖 Robot activado") 

   elif "temperatura" in text and "alta" in text:
      #Primero se comprueba que los sensores se encuentren encendidos
      if canvas.itemcget(temperatura, "fill") == "green":
         #Se modifica el color de los canvas y la etiqueta
         canvas.itemconfig(temperatura, fill="red")
         canvas.itemconfig(proximidad, fill="green")
         canvas.itemconfig(energia, fill="green")
         resultado_label.config(text="🌡️ La temperatura ha sido ajustada") 
         #Se muestra la alerta por temperatura demasiado elevada
         messagebox.showwarning("¡¡Alerta!!", "Temperatura elevada")
      else:
         resultado_label.config(text="El robot debe estar activo para continuar")

   elif "revisar" in text and "sensores" in text:
         #Se modifica la etiqueta
         resultado_label.config(text=estado_sensores(canvas.itemcget(temperatura, "fill"), canvas.itemcget(proximidad, "fill"), canvas.itemcget(energia, "fill")))

   elif "detener" in text and "robot" in text:
      #Se modifica el color de los canvas y la etiqueta
      canvas.itemconfig(temperatura, fill="grey20")
      canvas.itemconfig(proximidad, fill="grey20")
      canvas.itemconfig(energia, fill="grey20")
      resultado_label.config(text="💤 Robot desactivado") 

   elif "salir" in text:
      #Se modifica la etiqueta y se cierra la ventana
      resultado_label.config(text="👋 Cerrando programa...") 
      ventana.after(1000, ventana.destroy)
      
   else:
      #Se modifica la etiqueta
      resultado_label.config(text=" Comando no reconocido")


def estado_sensores(estadoTemp, estadoProx, estadoEnergia):
   """
   Comprueba el estado actual de los sensores y, en función del resultado
   devuelve un mensaje u otro
   """
   mensaje="Revisando sensores...\n"

   if estadoTemp=="grey20" and estadoProx=="grey20" and estadoEnergia=="grey20":
      mensaje+="Los sensores se encuentran actualmente apagados"
   elif estadoTemp=="green" and estadoProx=="green" and estadoEnergia=="green":
      mensaje+="Temperatura: Ambiental\nProximidad: No se ha encontrado ningún objeto\nEnergía: Estable"
   elif estadoTemp=="red" and estadoProx=="green" and estadoEnergia=="green":
      mensaje+="Temperatura: Demasiado alta (alerta)\nProximidad: No se ha encontrado ningún objeto\nEnergía: Estable"
   
   return mensaje
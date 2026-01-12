from modules.gui_manager import crear_ventana
from modules.audio_manager import escuchar
from modules.command_processor import procesar_comando
import tkinter as tk

def main():
 # Creamos la ventana y obtenemos los widgets
 ventana, canvas, temperatura, proximidad, energia, texto_label, resultado_label = crear_ventana()
 # Función que se ejecuta al pulsar el botón "Escuchar"
 def ejecutar_reconocimiento():
    texto_label.config(text="🎧 Escuchando... Habla ahora")  #Modifica el texto de la etiqueta
    ventana.update() #Se actualiza la ventana
    text, audio = escuchar()
    
    #Mostrar lo que el sistema interpretó
    texto_label.config(text=f"Nuestro sistema de inteligencia interpreta: {text if text else'No se entendió'}")
    ventana.update()
    procesar_comando(text, audio, canvas, (temperatura, proximidad, energia), resultado_label, ventana)
 # Botón para activar reconocimiento
 boton = tk.Button(ventana, text="🎤 Escuchar", command=ejecutar_reconocimiento, 
    font=("Arial", 14), bg="#00ffcc", fg="black", width=15, height=2)
 boton.pack(pady=20)

 ventana.mainloop()

if __name__ == "__main__":
 main()
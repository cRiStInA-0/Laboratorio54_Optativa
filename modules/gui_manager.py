import tkinter as tk

def crear_ventana():
 """Crea la ventana principal con semáforo y devuelve los widgets principales."""
 ventana = tk.Tk() #Crea la ventana raíz. Es el contenedor principal.
 ventana.title("Robot industrial controlado por voz") #Define el título
 ventana.geometry("600x500") #Define el tamaño inicial
 ventana.config(bg="#1e1e1e") #Define el color de fondo

 # Título de la ventana
 titulo = tk.Label(ventana, text="CONTROL POR VOZ - ESTADO Y SENSORES", #Texto
    font=("Arial", 16, "bold"), bg="#1e1e1e", fg="#00ffcc") #Fuente y color tanto de fondo como de texto
 titulo.pack(pady=10) #Margen

 # Canvas donde se dibujarán las luces redondas del semáforo
 canvas = tk.Canvas(ventana, width=400, height=150, bg="#111", highlightthickness=0)
 canvas.pack(pady=20) #Posicionar el canvas en la ventana y ajustar el margen

 # Crear etiquetas para cada sensor
 canvas.create_text(75, 15, text="Temperatura", fill="white", font=("Arial", 10, "bold"))
 canvas.create_text(195, 15, text="Proximidad", fill="white", font=("Arial", 10, "bold"))
 canvas.create_text(315, 15, text="Energía", fill="white", font=("Arial", 10, "bold"))

 # Crear luces redondas (óvalos) apagadas inicialmente (grey20) para los sensores
 temperatura = canvas.create_oval(25, 30, 125, 130, fill="grey20") 
 proximidad = canvas.create_oval(145, 30, 245, 130, fill="grey20")
 energia = canvas.create_oval(265, 30, 365, 130, fill="grey20")

 # Label de instrucciones
 texto_label = tk.Label(ventana, text="Pulsa '🎤 Escuchar' y da un comando.", 
    font=("Arial", 12), bg="#1e1e1e", fg="white") #Fuente y color tanto de fondo como de texto
 texto_label.pack(pady=10) #Margen

 # Label para mostrar resultados de reconocimiento
 resultado_label = tk.Label(ventana, text="...", 
    font=("Arial", 14, "bold"), bg="#1e1e1e", fg="#00ffcc") #Fuente y color tanto de fondo como de texto
 resultado_label.pack(pady=10) #Margen

 # Devolvemos todos los widgets necesarios
 return ventana, canvas, temperatura, proximidad, energia, texto_label, resultado_label
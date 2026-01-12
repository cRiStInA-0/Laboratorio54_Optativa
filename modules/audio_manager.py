from vosk import Model, KaldiRecognizer
import sounddevice as sd
import json

# Configuración del modelo y tasa de muestreo
samplerate = 16000
model = Model("vosk-model-small-es-0.42") # Modelo Vosk en español
recognizer = KaldiRecognizer(model, samplerate)

def escuchar():
 """Graba 5 segundos de audio y devuelve el texto reconocido."""
 audio = sd.rec(int(5 * samplerate), samplerate=samplerate,
    channels=1, dtype='int16')
 sd.wait() # Espera a que termine la grabación

 #Función if por si reconoce una frase completa 
 #de lo grabado anteriormente
 if recognizer.AcceptWaveform(audio.tobytes()):
    result = json.loads(recognizer.Result()) #Se obtiene un JSON y se transforma en un diccionario de python
    return result.get("text", ""), audio #Se devuelve tanto el texto transformado como el audio grabado
 else:
    return "", audio #Se devuelve contenido vacío y el audio grabado